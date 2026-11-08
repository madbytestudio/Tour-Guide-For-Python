from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X = [
    [1, 40], [2, 45], [2, 50], [3, 55], [3, 60], [4, 65],
    [5, 70], [6, 75], [7, 80], [8, 85], [9, 90], [10, 95],
]
y = [
    "Gagal", "Gagal", "Gagal", "Gagal", "Gagal", "Gagal",
    "Lulus", "Lulus", "Lulus", "Lulus", "Lulus", "Lulus",
]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1
)

model = DecisionTreeClassifier(random_state=1)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))
print("Ramalan [8, 90]:", model.predict([[8, 90]])[0])
print("Ramalan [2, 50]:", model.predict([[2, 50]])[0])
