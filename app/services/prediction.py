import joblib
import os
import pandas as pd
from fastapi import HTTPException
from pydantic import BaseModel
from datetime import datetime

# SQLAlchemy pour BDD
from sqlalchemy import create_engine, Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# ----------------------------
# CONFIG BDD POSTGRESQL LOCALE
# ----------------------------
DB_USER = "postgres"
DB_PASS = "password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "futurisys_ml"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()

class MLInput(Base):
    __tablename__ = "ml_inputs"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    NumberofFloors = Column(Integer)
    NumberofBuildings = Column(Float)
    GFAPerFloor = Column(Float)
    PropertyGFATotal = Column(Integer)
    GFA_Prison_Incarceration = Column(Float)
    GFA_College_University = Column(Float)
    GFA_Office = Column(Float)
    GFA_Parking = Column(Float)
    GFA_Medical_Office = Column(Float)
    GFA_Indoor_Arena = Column(Float)
    GFA_Hospital_General_Medical_Surgical = Column(Float)
    GFA_Data_Center = Column(Float)
    GFA_Laboratory = Column(Float)
    GFA_Supermarket_Grocery_Store = Column(Float)
    GFA_Urgent_Care_Clinic_Other_Outpatient = Column(Float)
    BuildingType_Nonresidential_WA = Column(Float)
    ZipCode_infrequent_sklearn = Column(Float)
    EPAPropertyType_infrequent_sklearn = Column(Float)
    outputs = relationship("MLOutput", back_populates="input_row")

class MLOutput(Base):
    __tablename__ = "ml_outputs"
    id = Column(Integer, primary_key=True)
    input_id = Column(Integer, ForeignKey("ml_inputs.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    prediction = Column(Float)
    input_row = relationship("MLInput", back_populates="outputs")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)  # Crée les tables si elles n'existent pas

# ----------------------------
# CHARGER LE MODELE ML
# ----------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/model.joblib")

try:
    model_dict = joblib.load(MODEL_PATH)
    model = model_dict["model"]
    columns = model_dict["feature_names"]
    print("Modèle chargé avec succès")
except FileNotFoundError:
    model = None
    print("Modèle non trouvé, utilisez un modèle fictif pour tester.")

# ----------------------------
# Pydantic Input
# ----------------------------
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

# ----------------------------
# PREDICT + ENREGISTREMENT BDD
# ----------------------------
def predict(data: InputData) -> float:
    data_dict = data.model_dump()

    # Insert input dans BDD
    input_row = MLInput(**data_dict)
    session.add(input_row)
    session.commit()  # On commit pour récupérer l'ID

    # Si pas de modèle, prédiction factice
    if model is None:
        pred_value = 42
    else:
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

        X_row = []
        for col in columns:
            key = next((k for k, v in remap.items() if v == col), col)
            if key not in data_dict:
                raise HTTPException(
                    status_code=422,
                    detail=f"Feature manquante pour le modèle: {key}"
                )
            value = data_dict[key]
            if not isinstance(value, (int, float)):
                raise HTTPException(
                    status_code=422,
                    detail=f"Type incorrect pour la feature {key}: attendu int ou float, reçu {type(value).__name__}"
                )
            X_row.append(value)

        X = pd.DataFrame([X_row], columns=columns)
        pred_value = float(model.predict(X)[0])

    # Insert output dans BDD
    output_row = MLOutput(input_id=input_row.id, prediction=pred_value)
    session.add(output_row)
    session.commit()

    return pred_value
