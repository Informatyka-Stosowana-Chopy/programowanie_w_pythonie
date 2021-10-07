# TODO maybe it is good idea to make class 'Animals' and this class should inherit this class
import random


class Sheep:
    def __init__(self, init_pos_limit: float, sheep_move_dist: float):
        self.init_pos_limit = init_pos_limit
        self.sheep_move_dist = sheep_move_dist
        self.position = (self.__initialize_sheep_position(), self.__initialize_sheep_position())

    def __initialize_sheep_position(self) -> float:
        return random.uniform(-self.init_pos_limit, self.init_pos_limit)

    def choose_move_direction(self):
        """
        random (0-4) and assign nuber to direction f.g 1 == north
        :return:
        """
        pass
