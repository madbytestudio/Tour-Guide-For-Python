import statistics
import numpy as np

data = [70, 80, 85, 90, 95, 80, 100]

print("Stdev:", statistics.stdev(data))
print("Variance:", statistics.variance(data))
print("P25:", np.percentile(data, 25))
print("P75:", np.percentile(data, 75))
