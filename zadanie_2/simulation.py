from wolf import Wolf
from sheep import Sheep
from save_to_file import Save


# Decorator
def remove_json_if_exist(func):
    import json
    import os

    def wrapper(*args):
        if os.path.exists(os.path.join(os.getcwd(), "pos.json")):
            os.remove(os.path.join(os.getcwd(), "pos.json"))

        with open(os.path.join(os.getcwd(), "pos.json"), 'a') as file:
            json.dump([], file)

        func(*args)
    return wrapper


def remove_csv_if_exist(func):
    import os

    def wrapper(*args):
        if os.path.exists(os.path.join(os.getcwd(), "alive.csv")):
            os.remove(os.path.join(os.getcwd(), "alive.csv"))

        with open(os.path.join(os.getcwd(), "alive.csv"), 'a') as file:
            file.write('numer tury,liczba zywych owiec\n')

        func(*args)
    return wrapper


class Simulation:
    def __init__(self, round_number: int, number_of_sheep: int, init_pos_limit: float, sheep_move_dist: float, wolf_move_dist: float):
        self.round_number = round_number
        self.number_of_sheep = number_of_sheep
        self.init_pos_limit = init_pos_limit
        self.sheep_move_dist = sheep_move_dist
        self.wolf_move_dist = wolf_move_dist
        self.wolf = Wolf(self.wolf_move_dist)
        self.sheep = [Sheep(init_pos_limit, sheep_move_dist) for _ in range(self.number_of_sheep)]
        self.nearest_sheep_index: int = 0

    def search_nearest_sheep(self) -> list:
        """
        loop through all sheep and return position of nearest one
        :return: list with position of nearest sheep
        """
        index_of_nearest_sheep = 0
        nearest_sheep_distance = abs(self.wolf.position[0] - self.sheep[0].position[0]) \
                               + abs(self.wolf.position[1] - self.sheep[0].position[1])

        for i, sheep in enumerate(self.sheep):
            distance = abs(self.wolf.position[0] - sheep.position[0]) + abs(self.wolf.position[1] - sheep.position[1])
            if distance < nearest_sheep_distance:
                nearest_sheep_distance = distance
                index_of_nearest_sheep = i

        self.nearest_sheep_index = index_of_nearest_sheep
        return self.sheep[self.nearest_sheep_index].position

    def __print_round_info(self, turn: int):
        print(f"Tura: {turn}")
        print(f"Pozycja Wilka: [{round(self.wolf.position[0], 3)}, {round(self.wolf.position[1], 3)}]")
        print(f"Liczba żyjących owiec: {len(self.sheep)}")
        print(f"Wilk goni owcę: {self.nearest_sheep_index}\n")

    def one_simulation_round(self):
        """
        in this function it should be single round of simulation
        if Wolf.check_if_can_attack == True, then nearest sheep should be eaten
        :return:
        """
        for sheep in self.sheep:
            sheep.move()
        nearest_sheep_pos = self.search_nearest_sheep()
        if self.wolf.check_if_can_attack(nearest_sheep_pos):
            self.wolf.position = nearest_sheep_pos
            self.sheep.pop(self.nearest_sheep_index)
            print(f"Owca {self.nearest_sheep_index} została zjedzona!\n")
        else:
            self.wolf.move_to_nearest_sheep(nearest_sheep_pos)

    @remove_json_if_exist
    @remove_csv_if_exist
    def simulate(self):
        """
        this method play simulation as many time as given round
        :return:
        """
        for turn in range(self.round_number):
            if len(self.sheep) == 0:
                print("\n########################################")
                print("    Wszystkie owce zostały zjedzone!")
                print("########################################")
                return
            self.one_simulation_round()
            self.__print_round_info(turn + 1)  # to print index starting at 1
            data_to_save = {"round_no": turn + 1, "wolf_pos": self.wolf.position, "sheep_pos": [sheep.position for sheep in self.sheep]}
            # TODO: albo wartość None/null w przypadku owiec, które zostały pożarte).

            Save.to_json(data_to_save)
            Save.to_csv(turn, len(self.sheep))
