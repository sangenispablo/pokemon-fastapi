from fastapi import FastAPI

from app.domain.exceptions.pokemon_already_exists import PokemonAlreadyExistsError
from app.domain.exceptions.pokemon_not_found import PokemonNotFoundError
from app.infrastructure.api import health_router, pokemon_router
from app.infrastructure.api.exception_handlers import (
    pokemon_already_exists_handler,
    pokemon_not_found_handler,
)

app = FastAPI(
    title="Pokemon API",
    version="1.0.0",
)

app.add_exception_handler(
    PokemonAlreadyExistsError,
    pokemon_already_exists_handler,
)
app.add_exception_handler(
    PokemonNotFoundError,
    pokemon_not_found_handler,
)

app.include_router(pokemon_router.router)
app.include_router(health_router.router)
