from zadanie_2.wolf import Wolf
from zadanie_2.sheep import Sheep


class Simulation:
    def __init__(self, round_number: int, number_of_sheep: int, init_pos_limit: float, sheep_move_dist: float, wolf_move_dist: float):
        self.round_number = round_number
        self.number_of_sheep = number_of_sheep
        self.init_pos_limit = init_pos_limit
        self.sheep_move_dist = sheep_move_dist
        self.wolf_move_dist = wolf_move_dist
        self.wolf = Wolf(self.wolf_move_dist)
        self.sheep = [Sheep(init_pos_limit, sheep_move_dist) for x in range(self.number_of_sheep)]  # TODO list comprehension should work fine in this case
