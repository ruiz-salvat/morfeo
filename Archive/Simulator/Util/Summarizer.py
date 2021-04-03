from scipy import stats
from DataObjects.Summary import Summary


def summarize(array):
    #norm_values = [float(i)/max(array) for i in array]
    norm_values = array
    # TODO: normalize the values takes too much time, it should be done by a separate process
    summary = Summary(stats.tmean(norm_values), stats.tstd(norm_values), stats.skew(norm_values),
                      stats.kurtosis(norm_values), stats.entropy(norm_values))
    return summary
