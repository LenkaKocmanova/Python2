import pandas
import requests
import matplotlib.pyplot as plt

from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    accuracy_score,
)

#r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/movies.csv")
#open("movies.csv", "wb").write(r.content)

data = pandas.read_csv("movies.csv")
print(data.head())

X = data["text"]
y = data["genre"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

y_train.value_counts(normalize=True).plot(kind="bar")
#plt.show()

vec = CountVectorizer()
X_train = vec.fit_transform(X_train)
X_test = vec.transform(X_test)

df = pandas.DataFrame.sparse.from_spmatrix(X_train)
df.columns = vec.get_feature_names_out()
print(df)

clf = KNeighborsClassifier(n_neighbors=10)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

confusion_matrix(y_test, y_pred)

ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test, normalize="true")

print(f"accuracy: {round(accuracy_score(y_test, y_pred), 2)}", f"f1 score: {round(f1_score(y_test, y_pred, average='weighted'), 2)}")

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
pipeline = Pipeline(
    [
        #("vec", CountVectorizer(stop_words="english")),
        ("vec", TfidfVectorizer(ngram_range=(1,2))),
        ("clf", KNeighborsClassifier(n_neighbors=10)),
    ]
)
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(f"accuracy: {round(accuracy_score(y_test, y_pred), 2)}", f"f1 score: {round(f1_score(y_test, y_pred, average='weighted'), 2)}")
ConfusionMatrixDisplay.from_estimator(pipeline, X_test, y_test, normalize="true")

feature_names = pipeline["vec"].get_feature_names_out()
print("*")

print(list(enumerate(clf.classes_)))
#pipeline["clf"].fit(X_train, y_train)
neg_feats = sorted(zip(pipeline["clf"].coef_[4, :], feature_names))[:20]
pos_feats = sorted(zip(pipeline["clf"].coef_[4, :], feature_names), reverse=True)[:20]
df = pandas.DataFrame(neg_feats + pos_feats, columns=["importance", "feature"])
df = df.set_index("feature").sort_values("importance")
df.plot(kind="bar", figsize=(15, 5))
plt.show()