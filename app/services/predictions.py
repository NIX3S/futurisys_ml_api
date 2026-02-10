import joblib
import os
from fastapi import HTTPException
import pandas as pd
from pydantic import BaseModel
# Charger le modèle ML
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/model.joblib")

try:
    model_dict = joblib.load(MODEL_PATH)
    model = model_dict["model"]
    columns = model_dict["feature_names"]  # les colonnes attendues par le modèle
    print("Modèle chargé avec succès")
    print(columns)
except FileNotFoundError:
    model = None
    print("Modèle non trouvé, utilisez un modèle fictif pour tester.")

class InputData(BaseModel):
    NumberofFloors: int
    NumberofBuildings: float
    GFAPerFloor: float
    PropertyGFATotal: int
    GFA_Prison_Incarceration: float  # Python-friendly
    GFA_College_University: float
    GFA_Office: float
    GFA_Parking: float
    GFA_Medical_Office: float
    GFA_Indoor_Arena: float
    GFA_Hospital_General_Medical_Surgical: float
    GFA_Data_Center: float
    GFA_Laboratory: float
    GFA_Supermarket_Grocery_Store: float
    GFA_Urgent_Care_Clinic_Other_Outpatient: float
    BuildingType_Nonresidential_WA: float
    ZipCode_infrequent_sklearn: float
    EPAPropertyType_infrequent_sklearn: float


import pandas as pd
from fastapi import HTTPException

def predict(data):
    if model is None:
        return 42  # prédiction factice

    data_dict = data.model_dump()  # Pydantic v2

    # Remap pour correspondre exactement aux colonnes du modèle
    remap = {
    "GFA_Prison_Incarceration": "GFA_Prison/Incarceration",
    "GFA_College_University": "GFA_College/University",
    "GFA_Medical_Office": "GFA_Medical Office",
    "GFA_Hospital_General_Medical_Surgical": "GFA_Hospital (General Medical & Surgical)",
    "GFA_Supermarket_Grocery_Store": "GFA_Supermarket/Grocery Store",
    "GFA_Urgent_Care_Clinic_Other_Outpatient": "GFA_Urgent Care/Clinic/Other Outpatient",
    "BuildingType_Nonresidential_WA": "BuildingType_Nonresidential WA",
    "GFA_Indoor_Arena": "GFA_Indoor Arena",
    "GFA_Data_Center": "GFA_Data Center"
    }

    # Crée la ligne X dans le bon ordre pour le modèle
    X_row = []
    for col in columns:
        key = next((k for k, v in remap.items() if v == col), col)
        if key not in data_dict:
            raise HTTPException(
                status_code=422,
                detail=f"Feature manquante pour le modèle: {key}"
            )
        value = data_dict[key]
        # Vérifie que le type est correct
        if not isinstance(value, (int, float)):
            raise HTTPException(
                status_code=422,
                detail=f"Type incorrect pour la feature {key}: attendu int ou float, reçu {type(value).__name__}"
            )
        X_row.append(value)

    X = pd.DataFrame([X_row], columns=columns)

    return float(model.predict(X)[0])