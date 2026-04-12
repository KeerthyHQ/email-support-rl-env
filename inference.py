import os
import requests
from openai import OpenAI


def log_start():
    print(f"[START] task=email_support env=email-support model={os.environ.get('MODEL_NAME','gpt-3.5-turbo')}", flush=True)


def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)


def log_end(success, steps, score, rewards):
    rewards_str = ",".join([f"{r:.2f}" for r in rewards])
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}", flush=True)


def run():
    log_start()

    rewards = []
    steps = 0
    score = 0.0
    success = False

    try:
       
        API_BASE_URL = os.environ["API_BASE_URL"]
        API_KEY = os.environ["API_KEY"]
        MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-3.5-turbo")

      
        client = OpenAI(
            base_url=API_BASE_URL,
            api_key=API_KEY
        )

        # RESET
        res = requests.post("http://127.0.0.1:8000/reset")
        res.raise_for_status()
        data = res.json()

        email = data["observation"]["email"]
        done = False

        while not done and steps < 3:
            steps += 1

            #  LLM CALL 
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful customer support agent."},
                    {"role": "user", "content": f"Customer email: {email}\nWrite a helpful reply."}
                ],
                temperature=0.7,
                max_tokens=100,
            )

            reply = response.choices[0].message.content.strip()

            # STEP ENV
            res = requests.post(
                "http://127.0.0.1:8000/step",
                json={"action": {"reply": reply}},
            )
            res.raise_for_status()

            data = res.json()

            reward = float(data.get("reward", 0.0))
            done = data.get("done", False)
            email = data["observation"]["email"]

            rewards.append(reward)

            log_step(steps, reply, reward, done)

        if rewards:
            score = min(sum(rewards) / len(rewards), 1.0)

        success = score > 0.1

    except Exception as e:
        print(f"[ERROR] {e}", flush=True)
        success = False

    log_end(success, steps, score, rewards)


if __name__ == "__main__":
    run()