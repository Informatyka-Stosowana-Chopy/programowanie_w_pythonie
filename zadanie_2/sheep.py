import random
import logging
from direction import Direction
import copy

class Sheep:
    def __init__(self, init_pos_limit: float, sheep_move_dist: float):
        self.init_pos_limit = init_pos_limit
        self.sheep_move_dist = sheep_move_dist
        self.position = [self.__initialize_sheep_position(), self.__initialize_sheep_position()]

    def __initialize_sheep_position(self) -> float:
        logging.debug("Sheep - initialize position, return: float (-init_pos_limit, init_pos_limit)")
        random_numer = random.uniform(-self.init_pos_limit, self.init_pos_limit)
        logging.info(f"sheep starting possition: {random_numer}")
        return random_numer

    def move(self):
        """
        random (0-4) and assign number to direction f.g 1 == north
        :return:
        """
        logging.debug("Sheep - move")
        random_direction = random.randint(0, 4)
        previous_position = self.position.copy()
        # with python 3.10 it is possible to do switch case and it would be better in this case :)
        if random_direction == Direction.NORTH:
            self.position = [self.position[0], self.position[1] + self.sheep_move_dist]
        elif random_direction == Direction.SOUTH:
            self.position = [self.position[0], self.position[1] - self.sheep_move_dist]
        elif random_direction == Direction.EAST:
            self.position = [self.position[0] + self.sheep_move_dist, self.position[1]]
        elif random_direction == Direction.WEST:
            self.position = [self.position[0] - self.sheep_move_dist, self.position[1]]

        logging.info(f"sheep moved from {previous_position} to {self.position}")
