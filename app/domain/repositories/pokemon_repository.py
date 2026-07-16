from abc import ABC, abstractmethod

from app.domain.entities.pokemon import Pokemon


class PokemonRepository(ABC):
    @abstractmethod
    def save(self, pokemon: Pokemon) -> Pokemon:
        pass

    @abstractmethod
    def find_by_number(self, number: int) -> Pokemon | None:
        pass
