EMAIL_SCENARIOS = [

    {
        "category": "Refund",
        "priority": "High",
        "sentiment": "Frustrated",
        "email": "I received a damaged product. I want a refund.",
        "followups": [
            "When will my refund be processed?",
            "Will I receive a confirmation email once the refund is completed?"
        ],
        "closing": "Your refund request has been successfully initiated. You will receive a confirmation email shortly.",
        "expected_keywords": ["refund", "return", "damaged"],
        "difficulty_multiplier": 1.0
    },

    {
        "category": "Delivery",
        "priority": "Medium",
        "sentiment": "Concerned",
        "email": "My order hasn't arrived yet. What is the delivery status?",
        "followups": [
            "Can you tell me the expected delivery date?",
            "Thank you. Is there anything else I need to do?"
        ],
        "closing": "Your order is on the way and no further action is required from your side. Thank you for your patience.",
        "expected_keywords": ["order", "delivery", "status"],
        "difficulty_multiplier": 1.0
    },

    {
        "category": "Replacement",
        "priority": "High",
        "sentiment": "Disappointed",
        "email": "I received the wrong product instead of the item I ordered.",
        "followups": [
            "How do I return the incorrect product?",
            "When will the replacement be shipped?"
        ],
        "closing": "Your replacement request has been confirmed. You'll receive tracking details once the new item is shipped.",
        "expected_keywords": ["replacement", "return", "wrong product"],
        "difficulty_multiplier": 1.1
    },

    {
        "category": "Payment",
        "priority": "High",
        "sentiment": "Angry",
        "email": "I was charged twice for my order.",
        "followups": [
            "How long will it take to investigate this issue?",
            "When can I expect the extra charge to be refunded?"
        ],
        "closing": "We've initiated an investigation into the duplicate charge. Any confirmed extra payment will be refunded promptly.",
        "expected_keywords": ["refund", "payment", "investigate"],
        "difficulty_multiplier": 1.2
    },

    {
        "category": "Payment",
        "priority": "Critical",
        "sentiment": "Worried",
        "email": "My payment failed but the amount was deducted from my bank account.",
        "followups": [
            "Can you confirm whether my order was placed successfully?",
            "When will the deducted amount be returned to my account?"
        ],
        "closing": "Our payment team is reviewing your transaction. If the payment was unsuccessful, the deducted amount will be refunded automatically.",
        "expected_keywords": ["payment", "refund", "transaction"],
        "difficulty_multiplier": 1.2
    },

    {
        "category": "Account",
        "priority": "Medium",
        "sentiment": "Confused",
        "email": "I forgot my password and cannot access my account.",
        "followups": [
            "I didn't receive the password reset email.",
            "The reset link says it has expired. What should I do now?"
        ],
        "closing": "A new password reset link has been sent to your registered email address. Please use it within 30 minutes.",
        "expected_keywords": ["password", "reset", "account"],
        "difficulty_multiplier": 1.0
    },

    {
        "category": "Account Security",
        "priority": "High",
        "sentiment": "Anxious",
        "email": "My account has been locked after multiple failed login attempts.",
        "followups": [
            "How can I verify my identity to unlock the account?",
            "Approximately how long will it take to restore access?"
        ],
        "closing": "Your account has been verified and unlocked successfully. You may now log in using your credentials.",
        "expected_keywords": ["unlock", "account", "verification"],
        "difficulty_multiplier": 1.1
    },

    {
        "category": "Order Management",
        "priority": "Medium",
        "sentiment": "Neutral",
        "email": "I want to cancel my order before it gets shipped.",
        "followups": [
            "Has my cancellation request been submitted successfully?",
            "When will I receive my refund after cancellation?"
        ],
        "closing": "Your order has been cancelled successfully. If applicable, your refund will be processed within 5–7 business days.",
        "expected_keywords": ["cancel", "order", "refund"],
        "difficulty_multiplier": 1.0
    },

    {
        "category": "Refund",
        "priority": "High",
        "sentiment": "Frustrated",
        "email": "My refund was approved but I still haven't received the money.",
        "followups": [
            "Can you check the current refund status?",
            "Who should I contact if I don't receive the refund this week?"
        ],
        "closing": "We've escalated your refund request to our finance team. You'll receive an update as soon as the transaction is completed.",
        "expected_keywords": ["refund", "status", "investigate"],
        "difficulty_multiplier": 1.3
    },

    {
        "category": "Delivery",
        "priority": "Medium",
        "sentiment": "Hopeful",
        "email": "I want to change the delivery address for my order.",
        "followups": [
            "Has my delivery address been updated successfully?",
            "Will changing the address delay the delivery?"
        ],
        "closing": "Your delivery address has been updated successfully. We'll notify you if there are any changes to the delivery schedule.",
        "expected_keywords": ["address", "update", "delivery"],
        "difficulty_multiplier": 1.1
    }

]