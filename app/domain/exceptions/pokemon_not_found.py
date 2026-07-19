class PokemonNotFoundError(Exception):
    def __init__(self, number: int):
        super().__init__(f"Pokemon with number {number} was not found.")
