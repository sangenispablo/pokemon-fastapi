from app.domain.entities.pokemon import Pokemon
from app.domain.repositories.pokemon_repository import PokemonRepository


class InMemoryPokemonRepository(PokemonRepository):
    def __init__(self):
        self.pokemons: dict[int, Pokemon] = {}

    def save(self, pokemon: Pokemon) -> Pokemon:
        self.pokemons[pokemon.number] = pokemon
        return pokemon

    def find_by_number(self, number: int) -> Pokemon | None:
        return self.pokemons.get(number)
