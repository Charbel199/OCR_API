from pydantic import BaseModel


class CharacterInfo(BaseModel):
    character: str
    x: int
    y: int
    h: int
    w: int
