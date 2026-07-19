from app.domain.exceptions.pokemon_not_found import PokemonNotFoundError
from app.domain.repositories.pokemon_repository import PokemonRepository


class GetPokemonUseCase:
    def __init__(self, pokemon_repository: PokemonRepository):
        self.pokemon_repository = pokemon_repository

    def execute(self, number: int):
        pokemon = self.pokemon_repository.find_by_number(number)
        if pokemon is None:
            raise PokemonNotFoundError(number)

        return pokemon
