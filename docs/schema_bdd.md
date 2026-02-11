\# Schéma UML de la Base de Données Futurisys ML



```mermaid

erDiagram

MLInput {

int id

datetime timestamp

int NumberofFloors

float NumberofBuildings

float GFAPerFloor

int PropertyGFATotal

float GFA_Prison_Incarceration

float GFA_College_University

float GFA_Office

float GFA_Parking

float GFA_Medical_Office

float GFA_Indoor_Arena

float GFA_Hospital_General_Medical_Surgical

float GFA_Data_Center

float GFA_Laboratory

float GFA_Supermarket_Grocery_Store

float GFA_Urgent_Care_Clinic_Other_Outpatient

float BuildingType_Nonresidential_WA

float ZipCode_infrequent_sklearn

float EPAPropertyType_infrequent_sklearn

}



MLOutput {

int id

int input_id

datetime timestamp

float prediction

}



MLInput ||--o{ MLOutput : has

