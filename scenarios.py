EMAIL_SCENARIOS = [
    {
        "id": 1,
        "type": "order_issue",
        "email": "Hi, I ordered a phone last week but it hasn't arrived yet. Can you check the status?",
        "expected_keywords": ["order", "status", "delivery", "check"]
    },
    {
        "id": 2,
        "type": "refund_request",
        "email": "I received a damaged product. I want a refund immediately.",
        "expected_keywords": ["refund", "return", "sorry"]
    },
    {
        "id": 3,
        "type": "complaint",
        "email": "Your service is very slow. I'm not happy with the support.",
        "expected_keywords": ["apologize", "improve", "support"]
    },
    {
        "id": 4,
        "type": "general_query",
        "email": "Can you tell me your working hours?",
        "expected_keywords": ["hours", "time", "available"]
    }
]