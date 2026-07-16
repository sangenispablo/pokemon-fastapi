from app.application.use_cases.create_pokemon import CreatePokemonUseCase
from app.infrastructure.database.repositories.in_memory_pokemon_repository import (
    InMemoryPokemonRepository,
)

repository = InMemoryPokemonRepository()


def get_create_pokemon_use_case() -> CreatePokemonUseCase:
    return CreatePokemonUseCase(repository)
