from sklearn.ensemble import RandomForestClassifier

class RandomForestModel:
    def __init__(self, n_estimators=100, random_state=42):
        self.model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)

    def train(self, X_train, y_train):
        print("Training Random Forest Model...")
        self.model.fit(X_train, y_train)
        return self.model

    def predict(self, X_test):
        return self.model.predict(X_test)
