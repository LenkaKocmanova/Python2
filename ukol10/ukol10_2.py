import requests
import pandas
import matplotlib.pyplot as plt
import numpy
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/auto.csv")
open("auto.csv", "wb").write(r.content)

data = pandas.read_csv("auto.csv", na_values=["?"])
pandas.set_option('display.max_columns', None)
print(data.shape)
data = data.dropna()
print(data.shape)
#Origin: 1=USA, 2=Evropa, 3=Japonsko

df_pivot = pandas.pivot_table(data, index = "year", columns="origin", values="mpg", aggfunc=numpy.mean, margins = True)
print(df_pivot)
df_pivot.plot()
plt.show()

X = data.drop(columns=["origin", "name"])
y = data["origin"]

#oh_encoder = OneHotEncoder()
#X = oh_encoder.fit_transform(X)

#print(y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)

scaler = StandardScaler(with_mean=False)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = DecisionTreeClassifier(random_state=0)

clf = GridSearchCV(model, param_grid={'max_depth': [2,4,6,9,11,15,19,20,30,40,50,70,90,100], 'min_samples_leaf': numpy.arange(1, 15)})
clf.fit(X_train, y_train)

print(clf.best_params_)
print(round(clf.best_score_, 2))

y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred, average='micro'))

# {'max_depth': 4, 'min_samples_leaf': 8}
# nejlepší skore je 80%
# f1_score = 75%