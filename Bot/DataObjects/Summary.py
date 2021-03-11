class Summary:
    def __init__(self, mean, std, skewness, kurtosis, entropy):
        self.mean = mean
        self.std = std
        self.skewness = skewness
        self.kurtosis = kurtosis
        self.entropy = entropy

    def __repr__(self):
        return str(self.__dict__)
