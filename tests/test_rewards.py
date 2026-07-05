from env.rewards import calculate_reward


def test_reward_in_range():
    context = {
        "expected_keywords": ["refund"],
        "conversation_history": [],
        "difficulty_multiplier": 1.0,
        "priority": "High",
        "sentiment": "Frustrated"
    }

    reward, _ = calculate_reward(
        context,
        "Sorry, your refund has been processed."
    )

    assert 0 < reward < 1