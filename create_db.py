# create_db.py
from sqlalchemy import create_engine, Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
import os

# Configuration PostgreSQL via variables d'environnement
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "futurisys_ml")

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


def main():
    print(f"Connecting to database at {DB_HOST}:{DB_PORT} with user {DB_USER}")
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)
    print("Tables créées avec succès !")


if __name__ == "__main__":
    main()
