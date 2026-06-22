import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("archive (4)/placement-dataset.csv")

print(df.head())

X = df[["city", "cgpa", "iq"]]
y = df["placement"]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("encoder", OneHotEncoder(handle_unknown="ignore"))
            ]),
            ["city"]
        ),
        (
            "num",
            Pipeline([
                ("imputer", SimpleImputer(strategy="mean"))
            ]),
            ["cgpa", "iq"]
        )
    ]
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy =", accuracy_score(y_test, y_pred))

joblib.dump(model, "placement_model.pkl")

print("Model Saved Successfully")