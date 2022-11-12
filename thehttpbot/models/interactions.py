import enum
from pydantic import BaseModel as PydanticBaseModel

__all__ = (
    'InteractionType',
    'Interaction',
)


class BaseModel(PydanticBaseModel):
    class Config:
        extra = 'allow'


class InteractionType(enum.IntEnum):
    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5


class Interaction(BaseModel):
    id: str
    application_id: str
    type: InteractionType
    token: str
    version: int
