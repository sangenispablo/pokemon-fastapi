class PokemonAlreadyExistsError(Exception):
    def __init__(self, number: int):
        self.number = number
        super().__init__(f"Pokemon with number {number} already exists.")
