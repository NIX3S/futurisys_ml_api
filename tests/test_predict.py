# tests/test_predict.py
import pytest
from fastapi import HTTPException
from app.services.prediction import predict
from app.api.endpoints import InputData
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

# Données valides
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

def test_predict_valid():
    result = predict(valid_data)
    assert isinstance(result, float)

def test_predict_missing_column():
    # Supprime volontairement une feature
    invalid_dict = valid_data.model_dump()
    invalid_dict.pop("NumberofFloors")
    # Pydantic ne permet plus de créer l'objet → test via HTTP endpoint
    response = client.post("/predict", json=invalid_dict)
    assert response.status_code == 422
    assert any("Feature manquante" in msg for msg in response.json()["detail"])
    
def test_predict_wrong_type():
    invalid_dict = valid_data.model_dump()
    invalid_dict["NumberofFloors"] = "cinquante"
    response = client.post("/predict", json=invalid_dict)
    assert response.status_code == 422
    assert any("Input should be a valid integer" in msg for msg in response.json()["detail"])

def test_predict_edge_values():
    # Valeurs extrêmes
    edge_data = valid_data.model_copy(update={
        "NumberofFloors": 0,
        "NumberofBuildings": -1,
        "GFAPerFloor": 1e6
    })
    result = predict(edge_data)
    assert isinstance(result, float)    