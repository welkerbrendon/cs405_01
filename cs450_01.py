import difflib

from sklearn import datasets
from sklearn.naive_bayes import GaussianNB

from HardCodedClassifier import HardCodedClassifier

csv = False
response = input("Would you like to use your own CSV file? (y/n): ")
if(response.__contains__("n")):
    iris = datasets.load_iris()
else:
    file_name = input("Please enter the path to the CSV file: ")
    import csv
    import sys
    f = open(file_name)
    reader = csv.reader(f)
    item = []
    list_of_list = []
    for row in reader:
        for col in row:
            item.append(col)
        list_of_list.append(row)
    reader.close()
    csv = True

import numpy as np
from sklearn.model_selection import train_test_split
if(csv):
    data = []
    target = []
    for list in iris:
        data.append(list[0, len(iris) - 2])
        target.append(list[len(iris) - 1])
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=.3)
else:
    data_train, data_test, target_train, target_test = train_test_split(iris.data, iris.target, test_size=.3)

# classifier = HardCodedClassifier()
# model = classifier.fit()
# targets_predicted = model.predict(data_test)

classifier = GaussianNB()
model = classifier.fit(data_train, target_train)

targets_predicted = model.predict(data_test)
similarity_amount = difflib.SequenceMatcher(None, targets_predicted, target_test)
print(similarity_amount.ratio())