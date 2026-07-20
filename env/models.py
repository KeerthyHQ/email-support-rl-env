from pydantic import BaseModel
from typing import Dict, Any, List


class EmailAction(BaseModel):
    reply: str


class EmailObservation(BaseModel):

    email: str
    reward: float
    done: bool

    category: str
    priority: str
    sentiment: str

    task: str
    task_score: float
    keyword_matches: int

    step_count: int
    difficulty: float


class EmailState(BaseModel):

    step_count: int
    conversation_history: List[str]

    current_email: Dict[str, Any]
    current_task: Dict[str, Any]

    # Required for final evaluation
    total_reward: float = 0.0
    total_keyword_matches: int = 0