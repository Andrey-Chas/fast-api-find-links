from pydantic import BaseModel


class SomeText(BaseModel):
    text: str


data = {
    "email": "test@gmail.com"
}
