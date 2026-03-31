#api endpoints for the server

from server.environment import EmailEnvironment
from openenv.core.env_server import create_fastapi_app 
from models import EmailAction,EmailObservation



app=create_fastapi_app(
    EmailEnvironment,
    action_cls=EmailAction,
    observation_cls=EmailObservation
)
