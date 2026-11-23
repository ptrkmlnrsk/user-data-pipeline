from pydantic import BaseModel, Field


class PostResponse(BaseModel):
    userId: int = Field(strict=True)
    id: int = Field(strict=True)
    title: str
    body: str
