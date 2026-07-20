from env.tasks import TASKS
from env.graders import (
    grade_easy,
    grade_medium,
    grade_hard
)

from env.models import (
    EmailAction,
    EmailObservation,
    EmailState
)

from env.rewards import calculate_reward
from env.scenarios import EMAIL_SCENARIOS
from env.evaluation import generate_evaluation_report

import random


class EmailEnvironment:

    def __init__(self, **kwargs):
        self._state = None
        self._evaluation = None

    def reset(self):

        current_email = random.choice(EMAIL_SCENARIOS)
        current_task = random.choice(TASKS)

        self._state = EmailState(
            step_count=0,
            conversation_history=[],
            current_email=current_email,
            current_task=current_task,

            #evaluation metric
            total_reward=0.0,
            total_keyword_matches=0
        )

        self._evaluation = None

        return EmailObservation(
            email=current_email["email"],
            reward=0.0,
            done=False,

            category=current_email["category"],
            priority=current_email["priority"],
            sentiment=current_email["sentiment"],

            task=current_task["name"],
            task_score=0.0,
            keyword_matches=0,

            step_count=0,
            difficulty=current_email["difficulty_multiplier"]
        )

    def step(self, action: EmailAction):

        if self._state is None:
            return self.reset()

        state = self._state

        reply = (action.reply or "").lower()

        state.conversation_history.append(reply)

        state.step_count += 1

        context = {
            "email": state.current_email["email"],
            "expected_keywords": state.current_email["expected_keywords"],
            "difficulty_multiplier": state.current_email["difficulty_multiplier"],
            "category": state.current_email["category"],
            "priority": state.current_email["priority"],
            "sentiment": state.current_email["sentiment"],
            "conversation_history": state.conversation_history
        }

        reward, matches = calculate_reward(
            context,
            reply
        )

        # ----------------------------
        # NEW: Track cumulative metrics
        # ----------------------------

        state.total_reward += reward
        state.total_keyword_matches += matches

        task_name = state.current_task["name"]

        if task_name == "basic_response_quality":

            task_score = grade_easy(
                context,
                reply
            )

        elif task_name == "conversation_consistency":

            task_score = grade_medium(
                context,
                state.conversation_history
            )

        elif task_name == "issue_resolution_quality":

            task_score = grade_hard(
                context,
                reply
            )

        else:

            task_score = 0.5

        followups = state.current_email.get("followups", [])

        if state.step_count <= len(followups):

            next_email = followups[state.step_count - 1]
            done = False

        else:

            next_email = state.current_email.get(
                "closing",
                "Thank you for contacting us."
            )

            done = True

        # ----------------------------
        # Generate final evaluation
        # ----------------------------

        if done:

            self._evaluation = generate_evaluation_report(
                total_reward=state.total_reward,
                total_turns=len(state.conversation_history),
                keyword_matches=state.total_keyword_matches,
                expected_keywords=len(
                    state.current_email["expected_keywords"]
                ),
                task_score=task_score,
                scenario=context["category"],
                difficulty=state.current_task["difficulty"],
                completed=True
            )

        else:

            self._evaluation = None

        return EmailObservation(

            email=next_email,

            reward=reward,
            done=done,

            category=context["category"],
            priority=context["priority"],
            sentiment=context["sentiment"],

            task=task_name,
            task_score=task_score,
            keyword_matches=matches,

            step_count=state.step_count,
            difficulty=context["difficulty_multiplier"]
        )

    def state(self):
        return (
            self._state.model_dump()
            if self._state
            else {}
        )

    def load_state(self, state):

        if state:
            self._state = EmailState(**state)

    async def reset_async(self):
        return self.reset()

    async def step_async(self, action):
        return self.step(action)

    def evaluation(self):
        return self._evaluation

    def close(self):
        return None