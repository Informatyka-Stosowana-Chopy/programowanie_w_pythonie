from data_analyzer import DataAnalyzer
###########################
# CONSTANT
###########################
FILE_NAME = "data/data.csv"

data = DataAnalyzer(FILE_NAME)

data.make_distribution_measures()
print(data.distribution_measures_table)
