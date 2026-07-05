# 🤖 AI Email Support Evaluation Environment

A Reinforcement Learning inspired environment for evaluating AI-powered customer support agents.

The environment simulates real-world customer support conversations and scores responses based on:

- Relevance
- Keyword matching
- Politeness
- Issue resolution
- Conversation consistency

---

## 🚀 Features

- Multi-turn customer support conversations
- Reward-based evaluation system
- Task-specific graders
- Support for multiple customer issue scenarios
- FastAPI backend
- Docker support
- Automated tests using Pytest
- Interactive web UI

---

## 📂 Project Structure

```text
email-support-rl-env/
│
├── env/
│   ├── env.py
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
├── tests/
│   ├── test_rewards.py
│   └── test_graders.py
│
├── UI/
│   └── index.html
│
├── docs/
│   └── architecture.png
│
├── screenshots/
│
├── inference.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🏗 Architecture

```text
Customer Email
      ↓
Inference Agent
      ↓
LLM Response Generation
      ↓
Environment Evaluation
      ↓
Reward Calculation
      ↓
Task Grading
      ↓
Next Observation
```

---

## 📧 Supported Scenarios

The environment currently supports:

- Refund requests
- Delayed delivery
- Wrong product received
- Duplicate payment
- Payment deduction issues
- Password reset
- Account lockout
- Order cancellation
- Refund status inquiries
- Address change requests

---

## 🧠 Reward Function

Rewards are computed using:

| Component | Reward |
|----------|--------|
| Keyword Match | +1.0 |
| Politeness | +0.5 |
| Multiple Keywords | +1.5 |
| Resolution Bonus | +1.0 |
| Repetition Penalty | -0.5 |
| Short Reply Penalty | -0.5 |

Rewards are normalized into the range:

```text
0.01 → 0.99
```

---

## 🎯 Evaluation Tasks

The environment evaluates agents across three dimensions:

### 1. Basic Response Quality
Measures:
- relevance
- keyword coverage
- politeness

### 2. Conversation Consistency
Measures:
- response diversity
- context retention
- conversation quality

### 3. Issue Resolution Quality
Measures:
- resolution effectiveness
- customer satisfaction
- completion likelihood

---

## 🛠 Installation

### Clone repository

```bash
git clone https://github.com/KeerthyHQ/email-support-rl-env.git
cd email-support-rl-env
```

### Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure OpenAI API Key

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

---

## ▶ Run FastAPI Server

```bash
uvicorn server.app:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

## 🤖 Run Inference Agent

```bash
python inference.py
```

---

## 🧪 Run Tests

```bash
pytest
```

Expected output:

```text
2 passed in 0.04s
```

---

## 🐳 Run with Docker

Build image:

```bash
docker build -t email-support-env .
```

Run container:

```bash
docker run -p 7860:7860 email-support-env
```

---

## 📊 Example Reward Output

```text
Customer:
I received a damaged product and need a refund.

Agent:
Sorry for the inconvenience. We will process your refund immediately.

Reward: 0.82
Task Score: 0.87
Keyword Matches: 2
```

---

## 🔮 Future Improvements

- Sentiment-aware rewards
- Dynamic customer personas
- LLM-as-a-judge evaluation
- Human feedback integration
- RL fine-tuning support
- Analytics dashboard

---

## 📌 Tech Stack

- Python
- FastAPI
- OpenAI API
- Pytest
- Docker
- HTML/CSS/JavaScript

---

## 👩‍💻 Author

Keerthika M

GitHub:
https://github.com/KeerthyHQ

---

## 📄 License

MIT License