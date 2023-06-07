from pydantic import BaseModel


class SomeText(BaseModel):
    text: str
