import json
import os
import csv


class Save:
    @staticmethod
    def to_json(dict_to_save: dict, dir_to_save: str):
        if dir_to_save is not None:
            PATH = dir_to_save
        else:
            PATH = os.path.join(os.getcwd(), "pos.json")

        # read file
        with open(PATH, 'r') as file:
            data = json.load(file)

        # update data
        data.append(dict_to_save)

        # save data
        with open(PATH, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def to_csv(turn: int, sheep_alive: int, dir_to_save: str):
        if dir_to_save is not None:
            PATH = dir_to_save
        else:
            PATH = os.path.join(os.getcwd(), "alive.csv")

        with open(PATH, 'a', newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([turn, sheep_alive])
