from typing import Dict, List


def calculate_grade(score: int) -> str:
    """Convert overall score into a letter grade."""

    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "Needs Improvement"


def generate_evaluation_report(
    *,
    total_reward: float,
    total_turns: int,
    keyword_matches: int,
    expected_keywords: int,
    task_score: float,
    scenario: str,
    difficulty: str,
    completed: bool,
) -> Dict:
    """
    Generate the final evaluation report after the
    conversation has finished.
    """

    keyword_accuracy = (
        (keyword_matches / expected_keywords) * 100
        if expected_keywords > 0
        else 0
    )

    task_completion = 100 if completed else 0

    conversation_consistency = round(task_score * 100)

    professional_tone = min(
        100,
        round(total_reward * 100)
    )

    response_quality = round(
        (
            conversation_consistency
            + professional_tone
            + keyword_accuracy
        ) / 3
    )

    overall_score = round(
        (
            keyword_accuracy * 0.25
            + conversation_consistency * 0.25
            + professional_tone * 0.20
            + response_quality * 0.15
            + task_completion * 0.15
        )
    )

    overall_score = min(overall_score, 100)

    strengths: List[str] = []

    if professional_tone >= 80:
        strengths.append("Professional and polite responses")

    if keyword_accuracy >= 70:
        strengths.append("Good use of relevant support terminology")

    if conversation_consistency >= 80:
        strengths.append("Maintained conversation context")

    if completed:
        strengths.append("Successfully resolved the customer's issue")

    suggestions: List[str] = []

    if keyword_accuracy < 70:
        suggestions.append(
            "Include more scenario-specific keywords."
        )

    if professional_tone < 80:
        suggestions.append(
            "Improve response tone and empathy."
        )

    if conversation_consistency < 80:
        suggestions.append(
            "Provide more consistent follow-up responses."
        )

    if not suggestions:
        suggestions.append(
            "Excellent performance. Keep it up!"
        )

    return {
        "overall_score": overall_score,
        "grade": calculate_grade(overall_score),
        "status": (
            "Conversation Resolved"
            if completed
            else "Incomplete"
        ),
        "scenario": scenario,
        "difficulty": difficulty,
        "total_turns": total_turns,
        "total_reward": round(total_reward, 2),
        "metrics": {
            "keyword_accuracy": round(keyword_accuracy),
            "conversation_consistency": conversation_consistency,
            "task_completion": task_completion,
            "professional_tone": professional_tone,
            "response_quality": response_quality,
        },
        "strengths": strengths,
        "suggestions": suggestions,
    }