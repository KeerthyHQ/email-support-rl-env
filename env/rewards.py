def calculate_reward(context, reply):
    reply = reply.lower()

    reward = 0.0
    matches = 0

 
    # 1. Keyword relevance
   
    for word in context["expected_keywords"]:
        if word.lower() in reply:
            reward += 1.0
            matches += 1

   
    # 2. Politeness score

    if any(word in reply for word in [
        "sorry",
        "thank you",
        "please",
        "apologize",
        "appreciate your patience"
    ]):
        reward += 0.5


    # 3. Short response penalty

    if len(reply.split()) < 5:
        reward -= 0.5


    # 4. Multiple keyword bonus

    if matches >= 2:
        reward += 1.0

    if matches >= 3:
        reward += 0.5


    # 5. Repetition penalty

    history = context.get("conversation_history", [])

    if history.count(reply) > 1:
        reward -= 0.5


    # 6. Resolution bonus

    if any(phrase in reply for phrase in [
        "refund processed",
        "issue resolved",
        "replacement initiated",
        "order cancelled",
        "password reset link sent"
    ]):
        reward += 1.0

    elif any(word in reply for word in [
        "refund",
        "resolve",
        "assist",
        "help",
        "support"
    ]):
        reward += 0.5


    # 7. Priority bonus

    if context.get("priority") == "Critical":
        reward += 0.3


    # 8. Sentiment-aware empathy bonus

    if context.get("sentiment") in [
        "Angry",
        "Frustrated",
        "Worried"
    ]:
        if any(word in reply for word in [
            "sorry",
            "apologize",
            "understand your frustration"
        ]):
            reward += 0.5


    # 9. Difficulty scaling

    reward *= context.get(
        "difficulty_multiplier",
        1.0
    )


    # 10. Normalize reward

    reward = max(
        0.01,
        min(reward / 5.0, 0.99)
    )

    return reward, matches