# tests/test_prediction.py
import pytest
from fastapi import HTTPException
from app.services import prediction
from app.api.endpoints import InputData

# ----------------------
# Données valides
# ----------------------
valid_data = InputData(
    NumberofFloors=50,
    NumberofBuildings=1,
    GFAPerFloor=500,
    PropertyGFATotal=500000,
    GFA_Prison_Incarceration=0,
    GFA_College_University=0,
    GFA_Office=0,
    GFA_Parking=0,
    GFA_Medical_Office=0,
    GFA_Indoor_Arena=0,
    GFA_Hospital_General_Medical_Surgical=0,
    GFA_Data_Center=0,
    GFA_Laboratory=0,
    GFA_Supermarket_Grocery_Store=0,
    GFA_Urgent_Care_Clinic_Other_Outpatient=0,
    BuildingType_Nonresidential_WA=0,
    ZipCode_infrequent_sklearn=0,
    EPAPropertyType_infrequent_sklearn=0
)

# ----------------------
# Cas 1: prédiction normale
# ----------------------
def test_predict_valid():
    result = prediction.predict(valid_data)
    assert isinstance(result, float)

# ----------------------
# Cas 2: prédiction factice si modèle None
# ----------------------
def test_predict_fallback(monkeypatch):
    monkeypatch.setattr(prediction, "model", None)
    result = prediction.predict(valid_data)
    assert result == 42

# ----------------------
# Cas 3: feature manquante
# ----------------------
def test_missing_feature(monkeypatch):
    # Remplace les colonnes pour forcer un KeyError
    monkeypatch.setattr(prediction, "columns", list(valid_data.model_dump().keys()) + ["fake_column"])
    with pytest.raises(HTTPException) as exc:
        prediction.predict(valid_data)
    assert exc.value.status_code == 422
    assert "Feature manquante" in exc.value.detail
