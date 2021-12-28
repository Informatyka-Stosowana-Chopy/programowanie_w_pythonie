import pandas as pd


class Reader:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_data(self) -> pd.DataFrame:
        try:
            # add header if doesn't exist
            self._add_headers_to_data()
            data_frame = pd.read_csv(self.file_path)
        except FileNotFoundError:
            return FileNotFoundError

        return data_frame

    def _add_headers_to_data(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            if lines[0] != "sex,length,diameter,height,whole weight,shucked weight,viscera weight,shell weight,rings\n":
                lines[0] = "sex,length,diameter,height,whole weight,shucked weight,viscera weight,shell weight,rings\n" + lines[0]

        if lines[0] != "sex,length,diameter,height,whole weight,shucked weight,viscera weight,shell weight,rings\n":
            with open(self.file_path, 'w') as file:
                file.writelines(lines)
