import tensorflow as tf
import pandas as pd
import numpy as np

from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import joblib


def get_risk_label(risk):
    if risk < 50:
        return "Low Risk"
    elif risk > 50 and risk < 70:
        return "Medium Risk"
    elif risk > 70 and risk < 90:
        return "High Risk"
    elif risk > 90 and risk < 100:
        return "Severe Risk"


class ProvathanModel:
    def __init__(self, model_path, min_max_path):
        self.MinMaxScalar = joblib.load(min_max_path)
        self.MinMaxScalar.clip = False
        self.model = keras.models.load_model(model_path)

    def predict(self, gender, age, CCP, RF, CRP, HAD, UA, ESR, RBC, WBC, HMC, HMG, PLT):
        if gender == "M":
            gender = True
        else:
            gender = False
        input = pd.DataFrame(
            {
                "gender": [gender],
                "age": [age],
                "CCP antibodies": [CCP],
                "RF": [RF],
                "C-reactive protein": [CRP],
                "Heredity Arthritis Disease": [HAD],
                "Uric Acid": [UA],
                "Erythrocyte sedimentation rate": [ESR],
                "RBC": [RBC],
                "WBC": [WBC],
                "Hematocrit": [HMC],
                "Hemoglobin": [HMG],
                "Platelets": [PLT],
            }
        ).astype("float32")

        normalized_input = self.MinMaxScalar.transform(input)
        result = self.model.predict(normalized_input)
        return float(result)


ProvathanModelInstance = ProvathanModel(
    model_path="./provathan_backend/DL/ra.h5",
    min_max_path="./provathan_backend/DL/minmax.pkl",
)
