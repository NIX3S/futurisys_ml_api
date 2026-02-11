````markdown

\# Futurisys ML API Documentation



\*\*Version :\*\* 0.1.0  

\*\*Base URL :\*\* `http://127.0.0.1:8000/`



---



\## POST /predict



\### Description

Effectue une prédiction avec le modèle ML Futurisys à partir des données de bâtiment fournies.  

La réponse renvoie la valeur prédite sous forme d’un `float`.



---



\### Request Body (application/json)



| Champ                                   | Type   | Description                              |

|----------------------------------------|--------|------------------------------------------|

| NumberofFloors                          | int    | Nombre d’étages                           |

| NumberofBuildings                       | float  | Nombre de bâtiments                       |

| GFAPerFloor                             | float  | Surface brute par étage                   |

| PropertyGFATotal                        | int    | Surface brute totale du bâtiment         |

| GFA\_Prison\_Incarceration                | float  | Surface pour prison/incarcération        |

| GFA\_College\_University                  | float  | Surface pour collège/université          |

| GFA\_Office                              | float  | Surface de bureaux                        |

| GFA\_Parking                             | float  | Surface de parking                        |

| GFA\_Medical\_Office                      | float  | Surface bureau médical                    |

| GFA\_Indoor\_Arena                        | float  | Surface arène intérieure                  |

| GFA\_Hospital\_General\_Medical\_Surgical  | float  | Surface hôpital général / chirurgie      |

| GFA\_Data\_Center                         | float  | Surface data center                        |

| GFA\_Laboratory                          | float  | Surface laboratoire                        |

| GFA\_Supermarket\_Grocery\_Store           | float  | Surface supermarché / épicerie            |

| GFA\_Urgent\_Care\_Clinic\_Other\_Outpatient | float | Surface soins urgents / clinique          |

| BuildingType\_Nonresidential\_WA          | float  | Type de bâtiment non résidentiel WA       |

| ZipCode\_infrequent\_sklearn              | float  | Code postal encodé                         |

| EPAPropertyType\_infrequent\_sklearn      | float  | Type de propriété encodé                   |



\#### Exemple JSON



```json

{

&nbsp; "NumberofFloors": 1,

&nbsp; "NumberofBuildings": 1,

&nbsp; "GFAPerFloor": 100,

&nbsp; "PropertyGFATotal": 1000,

&nbsp; "GFA\_Prison\_Incarceration": 0,

&nbsp; "GFA\_College\_University": 0,

&nbsp; "GFA\_Office": 0,

&nbsp; "GFA\_Parking": 0,

&nbsp; "GFA\_Medical\_Office": 0,

&nbsp; "GFA\_Indoor\_Arena": 0,

&nbsp; "GFA\_Hospital\_General\_Medical\_Surgical": 0,

&nbsp; "GFA\_Data\_Center": 0,

&nbsp; "GFA\_Laboratory": 0,

&nbsp; "GFA\_Supermarket\_Grocery\_Store": 0,

&nbsp; "GFA\_Urgent\_Care\_Clinic\_Other\_Outpatient": 0,

&nbsp; "BuildingType\_Nonresidential\_WA": 0,

&nbsp; "ZipCode\_infrequent\_sklearn": 0,

&nbsp; "EPAPropertyType\_infrequent\_sklearn": 0

}

````



---



\### Responses



| Code | Description                         | Exemple JSON                                                                              |

| ---- | ----------------------------------- | ----------------------------------------------------------------------------------------- |

| 200  | Prédiction réussie                  | `{ "prediction": 171801.93351229883 }`                                                    |

| 422  | Feature manquante ou type incorrect | `{ "detail": \["Feature manquante : NumberofFloors", "Type incorrect pour GFAPerFloor"] }` |

| 500  | Erreur interne du serveur           | `{ "detail": "Erreur interne du serveur" }`                                               |



---



\### Exemple Curl



```bash

curl -X POST "http://127.0.0.1:8000/predict" \\

-H "Content-Type: application/json" \\

-d '{

&nbsp; "NumberofFloors": 1,

&nbsp; "NumberofBuildings": 1,

&nbsp; "GFAPerFloor": 100,

&nbsp; "PropertyGFATotal": 1000,

&nbsp; "GFA\_Prison\_Incarceration": 0,

&nbsp; "GFA\_College\_University": 0,

&nbsp; "GFA\_Office": 0,

&nbsp; "GFA\_Parking": 0,

&nbsp; "GFA\_Medical\_Office": 0,

&nbsp; "GFA\_Indoor\_Arena": 0,

&nbsp; "GFA\_Hospital\_General\_Medical\_Surgical": 0,

&nbsp; "GFA\_Data\_Center": 0,

&nbsp; "GFA\_Laboratory": 0,

&nbsp; "GFA\_Supermarket\_Grocery\_Store": 0,

&nbsp; "GFA\_Urgent\_Care\_Clinic\_Other\_Outpatient": 0,

&nbsp; "BuildingType\_Nonresidential\_WA": 0,

&nbsp; "ZipCode\_infrequent\_sklearn": 0,

&nbsp; "EPAPropertyType\_infrequent\_sklearn": 0

}'

```



---



\### Notes



\* Tous les champs sont \*\*obligatoires\*\* et doivent être des `int` ou `float`.

\* Les erreurs de validation renvoient un code `422` avec un tableau détaillant chaque problème.

\* En cas de problème serveur (connexion à la base ou modèle non chargé), le code `500` est renvoyé.



```



