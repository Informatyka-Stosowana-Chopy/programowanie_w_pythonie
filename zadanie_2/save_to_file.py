import json
import os


class Save:
    @staticmethod
    def to_json(dict_to_save: dict):
        # read file
        with open(os.path.join(os.getcwd(), "pos.json"), 'r') as file:
            data = json.load(file)

        # update data
        data.append(dict_to_save)

        # save data
        with open(os.path.join(os.getcwd(), "pos.json"), 'w') as file:
            json.dump(data, file)

    @staticmethod
    def to_csv():
        pass
