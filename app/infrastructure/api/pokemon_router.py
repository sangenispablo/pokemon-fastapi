from fastapi import APIRouter, Depends, HTTPException, status

from app.application.use_cases.create_pokemon import CreatePokemonUseCase
from app.domain.exceptions.pokemon_already_exists import PokemonAlreadyExistsError
from app.infrastructure.api.schemas.pokemon_schema import CreatePokemonRequest
from app.infrastructure.dependencies.pokemon_dependencies import (
    get_create_pokemon_use_case,
)

router = APIRouter(prefix="/pokemon", tags=["Pokemon"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_pokemon(
    request: CreatePokemonRequest,
    use_case: CreatePokemonUseCase = Depends(get_create_pokemon_use_case),
):

    return use_case.execute(
        number=request.number,
        name=request.name,
    )
