#logic for the server environment

from openenv.core.env_server import Environment
from models import EmailAction,EmailObservation,EmailState 
from rewards import calculate_reward
from scenarios import EMAIL_SCENARIOS
import random

class EmailEnvironment(Environment):
    def __init__(self):
          #internal state initialization => Nothing in memory at start
        self._state = None 
        self.current_email = None

    def reset(self):
        #start a new email thread 

        #pick random scenario
        self.current_email = random.choice(EMAIL_SCENARIOS)
        self._state = EmailState(
            email = self.current_email["email"],
            step_count=0
        )

        return EmailObservation(
            email = self._state.email,
            reward=0,
            done=False,
            metadata={}
        )
    
    def step(self,action:EmailAction):
        #check self._state is not empty before incrementing
        if self._state is None:
            return EmailObservation(
                email = "Please call reset() function to proceed",
                reward=0,
                done=True,
                metadata={"error":"environment not initialised"}
            )
        #increment step count
        self._state.step_count+=1

        reply = action.reply
        #calculate reward for agent reply 
        reward,matches = calculate_reward(self.current_email,reply)
     
        #episode ends
        done=True

        return EmailObservation(
                email = self._state.email,
                reward=reward,
                done=done,
                metadata={
                    "step_count":self._state.step_count,
                    "email_type":self.current_email.get("type","unknown"),
                    "keyword_matches":matches,
                    "reply_length":len(reply.strip())
                    }
            )
    @property
    def state(self):
      return self._state
      