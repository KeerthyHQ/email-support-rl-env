from pydantic import BaseModel
from typing import Dict, Any, List

class EmailAction(BaseModel):
   
    #Action performed by the AI agent.
   
    reply: str


class EmailMetadata(BaseModel):

     #Additional information about the customer ticket.

    category: str
    priority: str
    sentiment: str
    task: str
    task_score: float
    keyword_matches: int
    step_count: int
    difficulty: float

class EmailObservation(BaseModel):
   
    #Observation returned by the environment after each step.

    email: str
    reward: float
    done: bool
    metadata: EmailMetadata


class EmailState(BaseModel):

    #Internal environment state maintained across conversation turns.
   
    step_count: int
    conversation_history: List[str]
    current_email: Dict[str, Any]
    current_task: Dict[str, Any]