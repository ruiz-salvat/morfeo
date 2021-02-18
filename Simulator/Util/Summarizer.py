from scipy import stats
from DataObjects.Summary import Summary


def summarize(array):
    summary = Summary(stats.tmean(array), stats.tstd(array), stats.skew(array), stats.kurtosis(array),
                      stats.entropy(array))
    return summary
