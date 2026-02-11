\# Documentation Technique du Modèle Futurisys ML



\## Modèle



\- \*\*Algorithme :\*\* Random Forest Regressor

\- \*\*Cible :\*\* Log-transformation de la valeur prédite (`log-target`)

\- \*\*Features utilisées :\*\* 18 variables liées aux bâtiments et propriétés (ex. NumberofFloors, PropertyGFATotal, GFA types, BuildingType\_Nonresidential\_WA, ZipCode\_infrequent\_sklearn, EPAPropertyType\_infrequent\_sklearn)

\- \*\*Encodage spécifique :\*\*

&nbsp; - Certaines colonnes catégorielles ont été encodées via scikit-learn (sklearn) pour les zip codes et types de propriétés.

&nbsp; - Transformation logarithmique appliquée sur la cible pour stabiliser la variance.



---



\## Performances du Modèle



\### R² (Coefficient de détermination)

| Jeu de données | R²       |

|----------------|----------|

| Train          | 0.9916   |

| Test           | 0.9860   |



\### Erreur absolue moyenne (MAE)

| Jeu de données | MAE       |

|----------------|-----------|

| Train          | 533,941.30 |

| Test           | 712,931.31 |



\### Erreur quadratique moyenne (RMSE)

| Jeu de données | RMSE       |

|----------------|------------|

| Train          | 1,521,379.29 |

| Test           | 1,803,996.35 |



\### Erreurs relatives

| Statistique                               | Valeur      |

|-------------------------------------------|------------|

| Moyenne erreur relative                    | 9.94%      |

| Médiane erreur relative                    | -1.16%     |

| % bâtiments avec erreur < ±10%            | 43.49%     |

| % bâtiments avec erreur < ±20%            | 69.44%     |

| % bâtiments avec erreur < ±50%            | 92.32%     |



\*\*Interprétation :\*\*

\- Le modèle est très performant sur les deux jeux de données (train et test) avec un R² proche de 1.

\- L’erreur relative moyenne reste faible (<10%) sur l’ensemble des bâtiments.

\- La médiane d’erreur relative proche de 0 indique que le modèle n’a pas de biais systématique important.

\- Plus de 92% des bâtiments ont une erreur inférieure à ±50%, ce qui est acceptable pour une estimation globale.



---



\## Maintenance et Suivi



\### Stockage

\- Le modèle est sauvegardé sous format `joblib` dans le dossier `models/` du projet.

\- Fichier : `model.joblib`

\- Contient :

&nbsp; - L’objet `RandomForestRegressor`

&nbsp; - La liste des noms de features (`feature\_names`)



\### Chargement

\- Le modèle est chargé via `joblib.load()` dans `app/services/prediction.py`

\- Vérifie la présence du fichier avant prédiction.

\- Si le modèle n’est pas disponible, une valeur fictive (`42`) est renvoyée pour permettre les tests de l’API.



\### Bonnes pratiques

\- \*\*Retrain :\*\* Prévoir un ré-entraînement si le dataset évolue significativement (nouveaux types de bâtiments, nouvelles régions, nouvelles métriques).

\- \*\*Sauvegarde :\*\* Conserver des versions datées pour pouvoir revenir en arrière.

\- \*\*Tests :\*\* Vérifier systématiquement R², MAE et RMSE après chaque ré-entraînement.

\- \*\*Surveillance :\*\* Comparer les prédictions avec les données réelles lorsque disponibles pour détecter tout drift du modèle.



---



\## Limitations connues



\- Les prédictions sur des bâtiments très atypiques peuvent présenter des erreurs plus élevées.

\- Le modèle est sensible à la qualité et à la cohérence des features fournies (ex. surfaces incohérentes, valeurs manquantes).

\- La transformation logarithmique peut provoquer des prédictions négatives si mal appliquée ou sur des inputs invalides.



