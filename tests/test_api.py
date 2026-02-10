import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Données valides
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

def test_predict_valid():
    response = client.post("/predict", json=valid_data)
    assert response.status_code == 200
    json_resp = response.json()
    assert "prediction" in json_resp
    assert isinstance(json_resp["prediction"], float)

def test_predict_missing_column():
    invalid_data = valid_data.copy()
    del invalid_data["NumberofFloors"]  # Supprime une colonne
    response = client.post("/predict", json=invalid_data)
    assert response.status_code == 422
    json_resp = response.json()
    assert any("Feature manquante" in msg for msg in json_resp["detail"])

def test_predict_wrong_type():
    invalid_data = valid_data.copy()
    invalid_data["NumberofFloors"] = "cinquante"
    response = client.post("/predict", json=invalid_data)
    assert response.status_code == 422
    json_resp = response.json()
    # Vérifie le message Pydantic plutôt que "Type incorrect"
    assert any("Input should be a valid integer" in msg for msg in json_resp["detail"])