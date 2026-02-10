# tests/test_endpoints.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.prediction import predict
from app.api.endpoints import InputData
from fastapi import HTTPException

client = TestClient(app)

# ----------------------
# Données valides
# ----------------------
valid_data = {
    "NumberofFloors": 50,
    "NumberofBuildings": 1,
    "GFAPerFloor": 500,
    "PropertyGFATotal": 500000,
    "GFA_Prison_Incarceration": 0,
    "GFA_College_University": 0,
    "GFA_Office": 0,
    "GFA_Parking": 0,
    "GFA_Medical_Office": 0,
    "GFA_Indoor_Arena": 0,
    "GFA_Hospital_General_Medical_Surgical": 0,
    "GFA_Data_Center": 0,
    "GFA_Laboratory": 0,
    "GFA_Supermarket_Grocery_Store": 0,
    "GFA_Urgent_Care_Clinic_Other_Outpatient": 0,
    "BuildingType_Nonresidential_WA": 0,
    "ZipCode_infrequent_sklearn": 0,
    "EPAPropertyType_infrequent_sklearn": 0
}

# ----------------------
# Test endpoint /predict avec données valides
# ----------------------
def test_predict_valid_endpoint():
    response = client.post("/predict", json=valid_data)
    assert response.status_code == 200
    json_resp = response.json()
    assert "prediction" in json_resp
    assert isinstance(json_resp["prediction"], float)

# ----------------------
# Test endpoint /predict avec feature manquante -> HTTP 422
# ----------------------
def test_predict_missing_feature():
    invalid_data = valid_data.copy()
    del invalid_data["NumberofFloors"]  # supprime une colonne obligatoire
    response = client.post("/predict", json=invalid_data)
    assert response.status_code == 422
    json_resp = response.json()
    assert "Feature manquante" in str(json_resp["detail"])

# ----------------------
# Test endpoint /predict avec type incorrect -> HTTP 422
# ----------------------
def test_predict_wrong_type():
    invalid_data = valid_data.copy()
    invalid_data["NumberofFloors"] = "cinquante"  # string au lieu d'int
    response = client.post("/predict", json=invalid_data)
    assert response.status_code == 422
    json_resp = response.json()
    assert any("Input should be a valid integer" in msg for msg in json_resp["detail"])

# ----------------------
# Test endpoint /predict pour erreur interne -> HTTP 500
# ----------------------
def test_predict_internal_error(monkeypatch):
    # Force une exception dans predict()
    def fake_predict(data):
        raise Exception("Erreur inattendue")

    monkeypatch.setattr("app.api.endpoints.predict", fake_predict)

    response = client.post("/predict", json=valid_data)
    assert response.status_code == 500
    json_resp = response.json()
    assert json_resp["detail"] == "Erreur interne du serveur"