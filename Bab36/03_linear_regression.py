from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [55, 60, 68, 75, 82]

model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction 6:", model.predict([[6]])[0])
