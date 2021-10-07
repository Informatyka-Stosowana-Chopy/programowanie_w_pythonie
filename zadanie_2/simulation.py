from wolf import Wolf
from sheep import Sheep


class Simulation:
    def __init__(self, round_number: int, number_of_sheep: int, init_pos_limit: float, sheep_move_dist: float, wolf_move_dist: float):
        self.round_number = round_number
        self.number_of_sheep = number_of_sheep
        self.init_pos_limit = init_pos_limit
        self.sheep_move_dist = sheep_move_dist
        self.wolf_move_dist = wolf_move_dist
        self.wolf = Wolf(self.wolf_move_dist)
        self.sheep = [Sheep(init_pos_limit, sheep_move_dist) for _ in range(self.number_of_sheep)]

    def one_simulation_round(self):
        """
        in this class it shoud be single round of simulation
        :return:
        """
        pass

    def simulate(self):
        """
        this method play simulation as many time as given round
        :return:
        """
        for turn in range(self.round_number):
            self.one_simulation_round()
