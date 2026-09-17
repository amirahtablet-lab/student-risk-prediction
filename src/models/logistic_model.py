from sklearn.linear_model import LogisticRegression

class LogisticModel:
    def __init__(self, random_state=42):
        self.model = LogisticRegression(random_state=random_state)

    def train(self, X_train, y_train):
        print("Training Logistic Regression Model...")
        self.model.fit(X_train, y_train)
        return self.model

    def predict(self, X_test):
        return self.model.predict(X_test)
