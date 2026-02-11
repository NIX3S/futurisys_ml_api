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

float GFA\_Prison\_Incarceration

float GFA\_College\_University

float GFA\_Office

float GFA\_Parking

float GFA\_Medical\_Office

float GFA\_Indoor\_Arena

float GFA\_Hospital\_General\_Medical\_Surgical

float GFA\_Data\_Center

float GFA\_Laboratory

float GFA\_Supermarket\_Grocery\_Store

float GFA\_Urgent\_Care\_Clinic\_Other\_Outpatient

float BuildingType\_Nonresidential\_WA

float ZipCode\_infrequent\_sklearn

float EPAPropertyType\_infrequent\_sklearn

}



MLOutput {

int id

int input\_id

datetime timestamp

float prediction

}



MLInput ||--o{ MLOutput : has

