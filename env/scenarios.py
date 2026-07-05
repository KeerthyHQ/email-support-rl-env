EMAIL_SCENARIOS = [
    {
        "category": "Refund",
        "priority": "High",
        "sentiment": "Frustrated",
        "email": "I received a damaged product. I want a refund.",
        "expected_keywords": ["refund", "return", "damaged"],
        "difficulty_multiplier": 1.0
    },

    {
        "category": "Delivery",
        "priority": "Medium",
        "sentiment": "Concerned",
        "email": "My order hasn't arrived yet. What is the delivery status?",
        "expected_keywords": ["order", "delivery", "status"],
        "difficulty_multiplier": 1.0
    },

    {
        "category": "Replacement",
        "priority": "High",
        "sentiment": "Disappointed",
        "email": "I received the wrong product instead of the item I ordered.",
        "expected_keywords": ["replacement", "return", "wrong product"],
        "difficulty_multiplier": 1.1
    },

    {
        "category": "Payment",
        "priority": "High",
        "sentiment": "Angry",
        "email": "I was charged twice for my order.",
        "expected_keywords": ["refund", "payment", "investigate"],
        "difficulty_multiplier": 1.2
    },

    {
        "category": "Payment",
        "priority": "Critical",
        "sentiment": "Worried",
        "email": "My payment failed but the amount was deducted from my bank account.",
        "expected_keywords": ["payment", "refund", "transaction"],
        "difficulty_multiplier": 1.2
    },

    {
        "category": "Account",
        "priority": "Medium",
        "sentiment": "Confused",
        "email": "I forgot my password and cannot access my account.",
        "expected_keywords": ["password", "reset", "account"],
        "difficulty_multiplier": 1.0
    },

    {
        "category": "Account Security",
        "priority": "High",
        "sentiment": "Anxious",
        "email": "My account has been locked after multiple failed login attempts.",
        "expected_keywords": ["unlock", "account", "verification"],
        "difficulty_multiplier": 1.1
    },

    {
        "category": "Order Management",
        "priority": "Medium",
        "sentiment": "Neutral",
        "email": "I want to cancel my order before it gets shipped.",
        "expected_keywords": ["cancel", "order", "refund"],
        "difficulty_multiplier": 1.0
    },

    {
        "category": "Refund",
        "priority": "High",
        "sentiment": "Frustrated",
        "email": "My refund was approved but I still haven't received the money.",
        "expected_keywords": ["refund", "status", "investigate"],
        "difficulty_multiplier": 1.3
    },

    {
        "category": "Delivery",
        "priority": "Medium",
        "sentiment": "Hopeful",
        "email": "I want to change the delivery address for my order.",
        "expected_keywords": ["address", "update", "delivery"],
        "difficulty_multiplier": 1.1
    }
]