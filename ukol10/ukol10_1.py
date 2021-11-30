import pandas

from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

data = pandas.read_csv("soybean-2-rot.csv")

X = data.drop(columns=["class"])
y = data["class"]

oh_encoder = OneHotEncoder()
X = oh_encoder.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)

clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f1_score(y_test, y_pred, average="weighted"))
print(clf.feature_importances_)
print(oh_encoder.feature_names_in_)
zipped = zip(oh_encoder.feature_names_in_, clf.feature_importances_)
zipped = list(zipped)
res = sorted(zipped, key = lambda x: x[1], reverse=True)
for name, importance in res:
    print(name, importance)

nejvetsi = res[0][0]
print(y.unique())
print(data[nejvetsi].unique())
#největší vliv má parametr temp nebo plant-stand.
X1 = data[nejvetsi]

oh_encoder1 = OneHotEncoder()
X1 = X1.values.reshape(-1,1)
X1 = oh_encoder1.fit_transform(X1)


X_train, X_test, y_train, y_test = train_test_split(
    X1, y, test_size=0.2, stratify=y, random_state=0
)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f1_score(y_test, y_pred, average="weighted"))
# Pokud použijeme jen parametr "temp", bude mít model přesnost jen 43%
# Pokud použijeme jen parametr "plant-stand", bude mít model přesnost 75%