from env.tasks import TASKS
from env.graders import (
    grade_easy,
    grade_medium,
    grade_hard
)

from env.models import (
    EmailAction,
    EmailObservation,
    EmailState,
    EmailMetadata
)

from env.rewards import calculate_reward
from env.scenarios import EMAIL_SCENARIOS

import random


class EmailEnvironment:

    def __init__(self, **kwargs):
        self._state = None

    def reset(self):

        current_email = random.choice(
            EMAIL_SCENARIOS
        )

        current_task = random.choice(
            TASKS
        )

        self._state = EmailState(
            step_count=0,
            conversation_history=[],
            current_email=current_email,
            current_task=current_task
        )

        return EmailObservation(
            email=current_email["email"],
            reward=0.0,
            done=False,

            metadata=EmailMetadata(
                category=current_email["category"],
                priority=current_email["priority"],
                sentiment=current_email["sentiment"],
                task=current_task["name"],
                task_score=0.0,
                keyword_matches=0,
                step_count=0,
                difficulty=current_email["difficulty_multiplier"]
            )
        )

    def step(self, action: EmailAction):

        if self._state is None:
            self.reset()

        state = self._state

        state.step_count += 1

        reply = (
            action.reply or ""
        ).lower()

        state.conversation_history.append(
            reply
        )

        context = {
            "email":
                state.current_email["email"],

            "expected_keywords":
                state.current_email[
                    "expected_keywords"
                ],

            "difficulty_multiplier":
                state.current_email[
                    "difficulty_multiplier"
                ],

            "category":
                state.current_email[
                    "category"
                ],

            "priority":
                state.current_email[
                    "priority"
                ],

            "sentiment":
                state.current_email[
                    "sentiment"
                ],

            "conversation_history":
                state.conversation_history
        }

        reward, matches = calculate_reward(
            context,
            reply
        )

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

        done = state.step_count >= 3

        return EmailObservation(
            email=state.current_email["email"],
            reward=reward,
            done=done,

            metadata=EmailMetadata(
                category=context["category"],
                priority=context["priority"],
                sentiment=context["sentiment"],
                task=task_name,
                task_score=task_score,
                keyword_matches=matches,
                step_count=state.step_count,
                difficulty=context["difficulty_multiplier"]
            )
        )

    def state(self):
        return (
            self._state.dict()
            if self._state
            else {}
        )

    def load_state(self, state):
        if state:
            self._state = EmailState(
                **state
            )

    async def reset_async(self):
        return self.reset()

    async def step_async(
        self,
        action
    ):
        return self.step(action)

    def close(self):
        return None