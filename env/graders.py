# graders.py
# Graders evaluate how well the agent performed for different task types.

from typing import List


def clamp(score: float) -> float:
 
    #Ensure score stays strictly between (0,1)
   
    return max(0.01, min(score, 0.99))



# EASY TASK
# Evaluate response quality

def grade_easy(context, reply):
    reply = reply.lower()
    score = 0.1

    # keyword relevance
    matches = sum(
        word.lower() in reply
        for word in context["expected_keywords"]
    )

    score += min(matches * 0.2, 0.6)

    # politeness
    if any(word in reply for word in [
        "sorry",
        "please",
        "thank you",
        "apologize"
    ]):
        score += 0.2

    # empathy bonus for unhappy customers
    if context.get("sentiment") in [
        "Angry",
        "Frustrated",
        "Worried"
    ]:
        if any(word in reply for word in [
            "sorry",
            "understand",
            "apologize"
        ]):
            score += 0.1

    return clamp(score)



# MEDIUM TASK
# Evaluate consistency across conversation

def grade_medium(context, history):
    score = 0.2

    # reward non-repetitive responses
    unique_replies = len(set(history))

    if unique_replies > 1:
        score += 0.3

    # politeness across entire conversation
    polite_count = sum(
        any(word in response.lower() for word in [
            "sorry",
            "please",
            "thank you"
        ])
        for response in history
    )

    score += min(polite_count * 0.1, 0.3)

    # reward progression in conversation
    if len(history) >= 3:
        score += 0.1

    return clamp(score)



# HARD TASK
# Evaluate actual issue resolution

def grade_hard(context, reply):
    reply = reply.lower()
    score = 0.2

    # keyword coverage
    matches = sum(
        word.lower() in reply
        for word in context["expected_keywords"]
    )

    score += min(matches * 0.15, 0.45)

    # strong resolution actions
    resolution_phrases = [
        "refund processed",
        "issue resolved",
        "replacement initiated",
        "order cancelled",
        "password reset link sent",
        "account unlocked",
        "delivery updated"
    ]

    if any(
        phrase in reply
        for phrase in resolution_phrases
    ):
        score += 0.3

    # customer support intent
    elif any(word in reply for word in [
        "refund",
        "assist",
        "help",
        "support",
        "resolve"
    ]):
        score += 0.15

    # higher expectations for critical tickets
    if context.get("priority") == "Critical":
        score += 0.05

    return clamp(score)