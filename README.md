🤖 AI Email Support Evaluation Environment

A Reinforcement Learning (RL)-inspired environment for evaluating AI-powered customer support agents through realistic multi-turn email conversations.










📖 Overview

The AI Email Support Evaluation Environment simulates realistic customer support conversations where an AI agent responds to customer emails over multiple turns.

Each response is automatically evaluated using a reward-based scoring system that measures:

🎯 Response relevance
🔑 Keyword matching
💬 Professional tone
✅ Issue resolution
🔄 Conversation consistency

The environment is designed for benchmarking customer-support AI agents and experimenting with reinforcement learning inspired evaluation workflows.

✨ Features
📧 Multi-turn customer support conversations
🤖 RL-inspired reward evaluation
📊 Interactive evaluation dashboard
🎯 Task-specific grading
📈 Performance metrics
📨 Multiple customer support scenarios
⚡ FastAPI backend
🌐 Interactive HTML/CSS/JavaScript frontend
🧪 Automated testing with Pytest
🐳 Docker support
🤗 Hugging Face deployment ready
📸 Screenshots
Environment Dashboard

screenshots/dashboard.png

Multi-turn Conversation

screenshots/conversation.png

Final Evaluation Report

screenshots/evaluation.png

🏗 Architecture
                Customer Email
                      │
                      ▼
            AI Support Agent
                      │
                      ▼
          Response Generation
                      │
                      ▼
        Reward & Keyword Evaluation
                      │
                      ▼
             Task-specific Graders
                      │
                      ▼
         Updated Conversation State
                      │
                      ▼
          Final Evaluation Report
📂 Project Structure
email-support-rl-env/
│
├── env/
│   ├── env.py
│   ├── evaluation.py
│   ├── rewards.py
│   ├── graders.py
│   ├── scenarios.py
│   ├── tasks.py
│   └── models.py
│
├── server/
│   ├── app.py
│   └── __init__.py
│
├── UI/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── tests/
│
├── screenshots/
│
├── Dockerfile
├── requirements.txt
├── inference.py
└── README.md

📧 Supported Customer Scenarios

Refund Request
Delayed Delivery
Wrong Product Received
Duplicate Payment
Payment Deducted but Order Failed
Password Reset
Account Locked
Order Cancellation
Refund Status
Address Change

🎯 Evaluation Tasks

The environment evaluates AI agents across three dimensions.

Task	Description
Basic Response Quality	Keyword relevance, politeness and clarity
Conversation Consistency	Context retention across multiple turns
Issue Resolution Quality	Resolution effectiveness and completion
🏆 Reward Function

Rewards are calculated using several evaluation signals.

Metric	Reward
Keyword Match	+1.0
Multiple Keywords	+1.5
Professional Tone	+0.5
Resolution Bonus	+1.0
Repetition Penalty	-0.5
Short Reply Penalty	-0.5

Normalized Reward Range

0.01 → 0.99
📊 Evaluation Dashboard

The environment generates a final evaluation report containing:

Overall Score
Grade
Resolution Status
Keyword Accuracy
Conversation Consistency
Task Completion
Professional Tone
Response Quality
Strengths
Suggestions