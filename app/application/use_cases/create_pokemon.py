from app.domain.entities.pokemon import Pokemon
from app.domain.exceptions.pokemon_already_exists import PokemonAlreadyExistsError
from app.domain.repositories.pokemon_repository import PokemonRepository


class CreatePokemonUseCase:
    def __init__(self, pokemon_repository: PokemonRepository):
        self.pokemon_repository = pokemon_repository

    def execute(self, number: int, name: str) -> Pokemon:
        existing_pokemon = self.pokemon_repository.find_by_number(number)
        if existing_pokemon:
            raise PokemonAlreadyExistsError(number)

        pokemon = Pokemon(number=number, name=name)
        return self.pokemon_repository.save(pokemon)
