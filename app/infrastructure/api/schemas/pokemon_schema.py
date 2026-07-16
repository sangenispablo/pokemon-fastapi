from pydantic import BaseModel, Field


class CreatePokemonRequest(BaseModel):
    number: int = Field(gt=0)
    name: str = Field(min_length=1)
