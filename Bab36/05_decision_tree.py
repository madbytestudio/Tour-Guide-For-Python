from sklearn.tree import DecisionTreeClassifier

X = [
    [1, 50], [2, 55], [3, 60], [4, 65], [5, 70],
    [6, 80], [7, 85], [8, 90], [9, 95], [10, 100],
]
y = [
    "Gagal", "Gagal", "Gagal", "Gagal", "Lulus",
    "Lulus", "Lulus", "Lulus", "Lulus", "Lulus",
]

model = DecisionTreeClassifier(random_state=1)
model.fit(X, y)

print(model.predict([[2, 55]])[0])
print(model.predict([[8, 90]])[0])
