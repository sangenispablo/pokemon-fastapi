from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.domain.exceptions.pokemon_already_exists import (
    PokemonAlreadyExistsError,
)


def pokemon_already_exists_handler(
    request: Request,
    exception: Exception,
) -> JSONResponse:
    if not isinstance(exception, PokemonAlreadyExistsError):
        raise exception

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": str(exception)},
    )
