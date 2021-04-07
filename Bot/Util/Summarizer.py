from scipy import stats
from DataObjects.Summary import Summary
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def summarize(array):
    np_array = np.array(array)
    reshaped_array = np_array.reshape(-1, 1)
    scaler = MinMaxScaler()
    norm_values = scaler.fit_transform(reshaped_array)
    summary = Summary(stats.tmean(norm_values), stats.tstd(norm_values), stats.skew(norm_values),
                      stats.kurtosis(norm_values), stats.entropy(norm_values))
    return summary
