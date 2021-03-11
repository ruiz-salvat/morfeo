from scipy import stats
from DataObjects.Summary import Summary


def summarize(array):
    #norm_values = [float(i)/max(array) for i in array]
    norm_values = array
    summary = Summary(stats.tmean(norm_values), stats.tstd(norm_values), stats.skew(norm_values),
                      stats.kurtosis(norm_values), stats.entropy(norm_values))
    return summary
