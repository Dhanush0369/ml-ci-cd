from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load data and train model
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Create versioned models
for version in [1, 2, 3, 4, 5]:
    model = LogisticRegression(max_iter=200 + version*100)  # Different params for versions
    model.fit(X_train, y_train)
    joblib.dump(model, f'models/v{version}/iris_model.pkl')
