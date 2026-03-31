#In and Out of the System  

from dataclasses import dataclass 
from typing import Dict,Any
from openenv.core.env_server import Action,Observation,State  

@dataclass
class EmailAction(Action):  
    #agent's action is to reply to an email
     reply: str

@dataclass 
class EmailObservation(Observation):
    #agent receives an email from environment response
    email:str
    reward :float
    done:bool
    metadata:Dict[str,Any] = None 

@dataclass 
class EmailState(State):
    #internal state like current email thread
    email:str
    step_count:int 
