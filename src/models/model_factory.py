from src.models.logistic_model import LogisticModel
from src.models.random_forest_model import RandomForestModel

class ModelFactory:
    @staticmethod
    def create(model_type: str):
        model_type = model_type.lower().strip()
        if model_type == "logistic":
            return LogisticModel()
        elif model_type in ["random_forest", "rf"]:
            return RandomForestModel()
        else:
            raise ValueError(f"Model type '{model_type}' tidak dikenali oleh Factory!")
