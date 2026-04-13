from statistics import mean, median, variance

def calculate_stats(data: list, col_names: list) -> list:
    data_mean, data_median, data_variance = ["mean"], ["median"], ["variance"]
    for index in range (len(data)):
        data_mean.append(mean(data[index]))
        data_median.append(median(data[index]))
        data_variance.append(variance(data[index]))
    return [col_names, data_mean, data_median, data_variance]

