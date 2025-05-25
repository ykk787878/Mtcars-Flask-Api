import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os

os.makedirs("model", exist_ok=True)
df = pd.read_csv("mtcars.csv", index_col=0)
X = df.drop("mpg", axis=1)
y = df["mpg"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model/model.pkl")
print("model saved to model/model.pkl")
