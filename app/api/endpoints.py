from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.prediction import predict
router = APIRouter()

# Modèle de validation Pydantic pour les données entrantes
class InputData(BaseModel):
    NumberofFloors: int
    NumberofBuildings: float
    GFAPerFloor: float
    PropertyGFATotal: int
    GFA_Prison_Incarceration: float  
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

class OutputData(BaseModel):
    prediction: float

@router.post("/predict", response_model=OutputData)
def make_prediction(data: InputData):
    try:
        result = predict(data)
        return {"prediction": result}
    except ValueError as ve:
        # Erreur liée aux features manquantes ou mal formées
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        # Autres erreurs inattendues
        #return {"error": str(e)}
        raise HTTPException(status_code=500, detail="Erreur interne du serveur")