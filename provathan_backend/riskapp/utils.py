import tensorflow as tf
import pandas as pd
import numpy as np

from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import joblib


def get_risk_label(risk):
    if risk < 40:
        return "Low Risk"
    elif risk > 40 and risk < 60:
        return "Medium Risk"
    elif risk > 60 and risk < 70:
        return "High Risk"
    elif risk > 70 and risk < 100:
        return "Severe Risk"


class ProvathanModel:
    def __init__(self, model_path, min_max_path):
        self.MinMaxScalar = joblib.load(min_max_path)
        self.MinMaxScalar.clip = False
        self.model = keras.models.load_model(model_path)

    def predict(self, sp02, temperature, CRP, HMG, WBC, PC, KD, HD, AD, RD):
        """
        Argument List
        -------------
        SP02 level: float
        Range: [ 30-100 ]
        Oxygen level in Blood

        Temperature: float
        Range: [96.0 - 106.0 ]
        Temperature of Human Body

        C-reactive protein: float
        Range: [ 0.0 - 5.0 ]
        C reactive portien (in mg/L)

        HMG: float
        Range: [ 13.5 - 18.0 ]
        Haemoglobin count in gm/dL

        WBC: float
        Range: [ 4.0 - 10.5 ]
        WBC count WBCs in the blood in WBCs per microliter

        PC: int
        Range: [ 150 - 450 ]

        KD: bool
        Has kidney Disease
        True or False

        HD: bool
        Has any kind of heart disease
        True or False

        AD: bool
        Has any kind of auto immunity disease
        True or False

        RD: bool
        Has any kind of Respiratory disease
        True or False
        """

        input = pd.DataFrame(
            {
                "sp02": [sp02],
                "temperature": [temperature],
                "C-reactive protein": [CRP],
                "haemoglobin": [HMG],
                "wbc_count": [WBC],
                "platelet count": [PC],
                "kidney disease": [KD],
                "heart disease": [HD],
                "auto immunity disease": [AD],
                "respiratory disease": [RD],
            }
        ).astype("float32")

        normalized_input = self.MinMaxScalar.transform(input)
        result = self.model.predict(normalized_input)
        return round(float(result), 4)


ProvathanModelInstance = ProvathanModel(
    model_path="./provathan_backend/DL/provathan model.h5",
    min_max_path="./provathan_backend/DL/minmax.pkl",
)
