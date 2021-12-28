import pandas as pd

from reader import Reader


class DataAnalyzer:
    def __init__(self, file_path: str):
        self.reader = Reader(file_path)
        self.observations = 4177
        self.data_frame = self.reader.read_data()
        self.sex_table = pd.DataFrame()
        self.distribution_measures_table = pd.DataFrame()

    def make_sex_table(self):
        male_count = 0
        infant_count = 0
        female_count = 0

        for data in self.data_frame['sex']:
            if data == 'M':
                male_count += 1
            if data == 'I':
                infant_count += 1
            if data == 'F':
                female_count += 1
        self.sex_table['sex'] = ['Male', 'Infant', 'Female']
        self.sex_table['count'] = [male_count, infant_count, female_count]
        self.sex_table['%'] = [round(male_count / self.observations * 100, 2),
                               round(infant_count / self.observations * 100, 2),
                               round(female_count / self.observations * 100, 2)]

    def make_distribution_measures(self):
        self.distribution_measures_table['name'] = ['length', 'diameter', 'height', 'whole weight', 'shucked weight',
                                                    'viscera weight', 'shell weight', 'rings']

        for name in self.distribution_measures_table['name']:
            # mean
            self.distribution_measures_table['mean'] = self.data_frame[name].mean()

            # standard deviation
            self.distribution_measures_table['std'] = self.data_frame[name].std()

            # minimum
            self.distribution_measures_table['min'] = self.data_frame[name].min()

            # quantile 25%
            self.distribution_measures_table['25%'] = self.data_frame[name].quantile(q=0.25)

            # quantile 50%
            self.distribution_measures_table['50%'] = self.data_frame[name].quantile(q=0.5)

            # quantile 75%
            self.distribution_measures_table['75%'] = self.data_frame[name].quantile(q=0.75)

            # maximum
            self.distribution_measures_table['max'] = self.data_frame[name].max()

    def prepare_all_table(self):
        self.make_sex_table()
        self.make_distribution_measures()
