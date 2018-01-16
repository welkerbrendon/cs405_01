class HardCodedClassifier():
    def fit(self):
        return self

    def predict(self, data_test):
        list = [0] * len(data_test)
        return list