from iris_analysis import load_data
from iris_analysis import save_data
from iris_analysis import calculate_stats

data, col_names = load_data("iris.csv")
save_data("results.csv", calculate_stats(data, col_names))