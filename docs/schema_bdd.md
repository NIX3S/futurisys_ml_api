\# Schéma UML de la Base de Données Futurisys ML



```mermaid

erDiagram

&nbsp;   MLInput {

&nbsp;       int id PK "Clé primaire"

&nbsp;       datetime timestamp "Date et heure de l'insertion"

&nbsp;       int NumberofFloors

&nbsp;       float NumberofBuildings

&nbsp;       float GFAPerFloor

&nbsp;       int PropertyGFATotal

&nbsp;       float GFA\_Prison\_Incarceration

&nbsp;       float GFA\_College\_University

&nbsp;       float GFA\_Office

&nbsp;       float GFA\_Parking

&nbsp;       float GFA\_Medical\_Office

&nbsp;       float GFA\_Indoor\_Arena

&nbsp;       float GFA\_Hospital\_General\_Medical\_Surgical

&nbsp;       float GFA\_Data\_Center

&nbsp;       float GFA\_Laboratory

&nbsp;       float GFA\_Supermarket\_Grocery\_Store

&nbsp;       float GFA\_Urgent\_Care\_Clinic\_Other\_Outpatient

&nbsp;       float BuildingType\_Nonresidential\_WA

&nbsp;       float ZipCode\_infrequent\_sklearn

&nbsp;       float EPAPropertyType\_infrequent\_sklearn

&nbsp;   }



&nbsp;   MLOutput {

&nbsp;       int id PK "Clé primaire"

&nbsp;       int input\_id FK "Référence à MLInput.id"

&nbsp;       datetime timestamp "Date et heure de la prédiction"

&nbsp;       float prediction "Valeur prédite par le modèle"

&nbsp;   }



&nbsp;   MLInput ||--o{ MLOutput : "produit"



