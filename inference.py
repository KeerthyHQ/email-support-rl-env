import os
import requests
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

API_URL = "http://127.0.0.1:8000"

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_reply(email):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content":
                    "You are a helpful customer support assistant."
            },

            {
                "role": "user",
                "content":
                    f"Customer email: {email}\nGenerate a professional reply."
            }
        ]
    )

    return response.choices[0].message.content


def run():

    reset_response = requests.post(
        f"{API_URL}/reset"
    )

    observation = reset_response.json()

    email = observation["observation"]["email"]

    done = False

    while not done:

        reply = generate_reply(email)

        step_response = requests.post(
            f"{API_URL}/step",
            json={
                "action": {
                    "reply": reply
                }
            }
        )

        result = step_response.json()

        reward = result["reward"]

        print(f"Reward: {reward}")

        done = result["done"]

        email = result["observation"]["email"]


if __name__ == "__main__":
    run()