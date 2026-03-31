#logic for the server environment

from openenv.core.env_server import Environment
from models import EmailAction,EmailObservation,EmailState 

class EmailEnvironment(Environment):
    def __init__(self):
          #internal state initialization => Nothing in memory at start
        self._state = None 

    def reset(self):
        #start a new email thread
        self._state = EmailState(
            email =" I have been Charged Twice for my product. Please help! ",
            step_count=0
        )

        return EmailObservation(
            email = self._state.email,
            reward=0,
            done=False,
            metadata={}
        )
    
    def step(self,action:EmailAction):
        #increment step count
        self._state.step_count+=1
        response = action.reply.lower()
        reward =0
        #reward logic 
        if "refund" in response:
            reward+=0.4
        if "apologize" in response or "sorry" in response:
            reward+=0.3
        if "help" in response:
            reward+=0.2
        if "compensate" in response:
            reward+=0.1
        #episode ends
        done=True

        return EmailObservation(
                email = self._state.email,
                reward=reward,
                done=done,
                metadata={"step_count":self._state.step_count}
            )
    @property
    def state(self):
      return self._state
      