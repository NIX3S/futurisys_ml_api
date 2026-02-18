```markdown
# FuturiSys ML API

API FastAPI connectée à PostgreSQL intégrant un modèle Machine Learning, avec pipeline CI/CD et déploiement automatique vers Hugging Face Spaces.

Ce projet permet de prédire la consommation énergétique de bâtiments à Seattle via une API REST.

---

##  Table of Contents

- [About The Project](#about-the-project)
- [Project Structure](#project-structure)
- [Built With](#built-with)
- [CI/CD Pipeline](#cicd-pipeline)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Creation](#database-creation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

##  About The Project

FuturiSys ML API est une API développée avec **FastAPI**, connectée à une base **PostgreSQL**, intégrant un modèle Machine Learning pour effectuer des prédictions sur la consommation énergétique de bâtiments à Seattle.

Fonctionnalités clés :

- Initialisation automatique de la base via SQLAlchemy  
- Tests automatisés avec Pytest  
- Couverture de code  
- Pipeline CI/CD GitHub Actions  
- Déploiement automatique vers Hugging Face Spaces  
- Chargement d’un modèle `.joblib` pour les prédictions

---

## 🏗 Project Structure

```

.
├── app/
│   ├── main.py
│   ├── exceptions.py
│   ├── api/
│   │   └── endpoints.py
│   ├── models/
│   │   └── model.joblib
│   └── services/
│       └── prediction.py
├── tests/
│   ├── test_api.py
│   ├── test_endpoint.py
│   ├── test_predict.py
│   └── test_prediction.py
├── create_db.py
├── requirements.txt
└── .github/workflows/ci.yml

```

###  Modèle Machine Learning

Le modèle est stocké localement dans :

```

app/models/model.joblib

````

Si absent, il peut être récupéré depuis Hugging Face :  
[https://huggingface.co/nix3s/futurisys_ml_model](https://huggingface.co/nix3s/futurisys_ml_model)

---

##  Built With

- Python 3.11  
- FastAPI  
- PostgreSQL 15  
- SQLAlchemy  
- Psycopg  
- Pytest  
- Uvicorn  
- GitHub Actions  
- Hugging Face Spaces  

---

##  CI/CD Pipeline

Le pipeline GitHub Actions se déclenche sur :

- `push` vers `main`
- `push` vers `feature/*`

### Étapes automatisées :

1. Lancement d’un service PostgreSQL (container)  
2. Installation des dépendances  
3. Attente que PostgreSQL soit prêt  
4. Création de la base si elle n’existe pas  
5. Initialisation des tables via `create_db.py`  
6. Exécution des tests avec couverture  
7. Déploiement automatique vers Hugging Face via SSH  

---

##  Getting Started

###  Prerequisites

- Python 3.11  
- PostgreSQL  
- pip  

Mettre à jour pip :

```bash
python -m pip install --upgrade pip
````

---

###  Installation

1. Cloner le repository

```bash
git clone https://github.com/your_username/futurisys_ml_api.git
cd futurisys_ml_api
```

2. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🗄 Database Creation

Créer la base PostgreSQL si elle n’existe pas :

```bash
createdb -U postgres futurisys_db
```

Ou via psql :

```sql
CREATE DATABASE futurisys_db;
```

Ensuite initialiser les tables :

```bash
python create_db.py
```

---

##  Environment Variables

Créer un fichier `.env` à la racine du projet :

```env
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=futurisys_db
DATABASE_URL=postgresql+psycopg2://your_user:your_password@localhost:5432/futurisys_db
```

---

##  Usage

Lancer le serveur FastAPI :

```bash
uvicorn app.main:app --reload
```

API disponible sur :

```
http://127.0.0.1:8000
```

Documentation interactive Swagger :

```
http://127.0.0.1:8000/docs
```

---

##  Testing

Exécuter les tests :

```bash
pytest --cov=app tests/
```

Les tests couvrent :

* API
* Endpoints
* Service de prédiction
* Logique métier

---

##  Deployment

Le déploiement vers Hugging Face Spaces est automatique via GitHub Actions.

Étapes principales :

1. Connexion SSH via `HF_SSH_KEY`
2. Clone du Space :

```bash
git@hf.co:spaces/nix3s/futurisys_ml_api.git
```

3. Copie des fichiers
4. Commit automatique
5. Push vers `main`

Chaque push validé déclenche une mise à jour du Space.

---

## 🛣 Roadmap

* Dockerisation complète
* Monitoring
* Authentification JWT
* Documentation OpenAPI avancée

---

##  Contributing

```bash
git checkout -b feature/AmazingFeature
git commit -m "Add AmazingFeature"
git push origin feature/AmazingFeature
```

Ouvrir ensuite une Pull Request sur GitHub.

---

##  License

Distribué sous licence MIT.

---

##  Contact

Paul Lesage
GitHub: [https://github.com/nix3s](https://github.com/nix3s)
Project Link: [https://github.com/nix3s/futurisys_ml_api](https://github.com/nix3s/futurisys_ml_api)

```
