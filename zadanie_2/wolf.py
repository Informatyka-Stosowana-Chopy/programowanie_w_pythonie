class Wolf:
    def __init__(self, wolf_move_dist: float):
        self.position = [0.0, 0.0]
        self.wolf_move_dist = wolf_move_dist

    def check_if_can_attack(self, nearest_sheep_pos: list) -> bool:
        """
        it check if it possible to attack nearest sheep
        if sheep is in range wolf_move_dist it returns True
        else return False
        :return:
        """
        # TODO check if it is good. probably it should check sqrt(2) to make an radius not in linear
        if (abs(self.position[0] - nearest_sheep_pos[0]) <= self.wolf_move_dist and abs(self.position[1] <=
            nearest_sheep_pos[1])) or abs(self.position[1] - nearest_sheep_pos[1]) <= self.wolf_move_dist and \
                abs(self.position[0] <= nearest_sheep_pos[0]):
            return True
        return False

    def move_to_nearest_sheep(self, sheep_position: list):
        """
        it should move
        :return:
        """
        # sheep_pos - woolf_pos = [x, y] then if x > y move to x else to y
        distance = [abs(sheep_position[0] - self.position[0]), abs(sheep_position[1] - self.position[1])]

        # in this case we check if it is better to move in x or y direction
        if distance[0] >= distance[1]:
            pos = 0
        else:
            pos = 1

        # there we check if it move in + or - direciton
        if sheep_position[pos] > self.position[pos]:
            self.position[pos] = self.position[pos] + self.wolf_move_dist
        else:
            self.position[pos] = self.position[pos] - self.wolf_move_dist

        # TODO make test to check if it is working, probably I made a mistake with +/- or </> somewhere
