import pandas
import requests
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import LinearSVC

#r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/soybean-1-spot.csv")
#open("soybean-1-spot.csv", "wb").write(r.content)

#r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/soybean-2-rot.csv")
#open("soybean-2-rot.csv", "wb").write(r.content)

data = pandas.read_csv("soybean-1-spot.csv")
X = data.drop(columns=["class"])
y = data["class"]
print(y.value_counts())
encoder = OneHotEncoder()
X = encoder.fit_transform(X)
print(pandas.DataFrame(X.toarray(), columns=encoder.get_feature_names_out()).head())
encoder = LabelEncoder()
y = encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
#clf = KNeighborsClassifier()
#print(clf.fit(X_train, y_train))
#y_pred = clf.predict(X_test)

model_1 = KNeighborsClassifier()
params_1 = {"n_neighbors": [1, 5, 7, 11, 13]}

clf_1 = GridSearchCV(model_1, params_1, scoring="f1_weighted")
clf_1.fit(X_train, y_train)

print(clf_1.best_params_)
print(round(clf_1.best_score_, 2))