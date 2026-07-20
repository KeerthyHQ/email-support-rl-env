from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from env.env import EmailEnvironment
from env.models import EmailAction

app = FastAPI(title="AI Email Support Environment")

# Persistent environment
environment = EmailEnvironment()

app.mount("/UI", StaticFiles(directory="UI"), name="UI")


@app.get("/")
def home():
    return FileResponse("UI/index.html")


@app.post("/reset")
def reset():

    observation = environment.reset()

    return {
        "observation": observation.model_dump(),
        "reward": observation.reward,
        "done": observation.done,
        "evaluation": None
    }


@app.post("/step")
def step(action: dict):

    email_action = EmailAction(
        **action.get("action", {})
    )

    observation = environment.step(email_action)

    return {
        "observation": observation.model_dump(),
        "reward": observation.reward,
        "done": observation.done,
        "evaluation": environment.evaluation()
    }


@app.get("/state")
def state():
    return environment.state()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )