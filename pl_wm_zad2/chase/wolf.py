from math import sqrt
import logging

class Wolf:
    def __init__(self, wolf_move_dist: float):
        self.position = [0.0, 0.0]
        logging.info("Wolf starting position = [0.0, 0.0]")
        self.wolf_move_dist = wolf_move_dist

    def check_if_can_attack(self, nearest_sheep_pos: list) -> bool:
        """
        it check if it possible to attack nearest sheep
        if sheep is in range wolf_move_dist it returns True
        else return False
        :return:
        """
        logging.debug(f"Wolf - check if can attack arg: nearest_sheep_pos = {nearest_sheep_pos}, return: bool")
        if sqrt((self.position[0] - nearest_sheep_pos[0])**2 + (self.position[1] - nearest_sheep_pos[1])**2) <= self.wolf_move_dist:
            return True
        return False

    def move_to_nearest_sheep(self, sheep_position: list):
        """
        it should move
        :return:
        """
        logging.debug(f"Wolf - move to nearest sheep arg: sheep_position = {sheep_position}")
        # sheep_pos - woolf_pos = [x, y]
        distance = [sheep_position[0] - self.position[0], sheep_position[1] - self.position[1]]

        distance_between_points = sqrt((self.position[0] - sheep_position[0]) ** 2 + (self.position[1] - sheep_position[1]) ** 2)

        x_to_move = (self.wolf_move_dist * distance[0])/ distance_between_points
        y_to_move = (self.wolf_move_dist * distance[1]) / distance_between_points
        logging.info(f"Wolf moved from {self.position} to [{self.position[0] + x_to_move}, {self.position[1] + y_to_move}]")
        self.position[0] += x_to_move
        self.position[1] += y_to_move
