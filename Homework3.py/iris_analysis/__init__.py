' This package can be used to load Iris data, calculate its basic statistics and save them to .csv file.'
from iris_analysis.io import load_data
from iris_analysis.io import save_data
from .calculate import calculate_stats
__all__ = ("load_data", "save_data", "calculate_stats")