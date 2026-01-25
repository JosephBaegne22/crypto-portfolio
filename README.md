# Crypto Portfolio Manager

## Description

Ce projet est une application web de gestion de portefeuille de cryptomonnaies.  
Elle permet à un utilisateur de s’inscrire, se connecter et gérer ses actifs crypto dans un espace personnel sécurisé.

L’application offre une vue claire de la valeur globale du portefeuille et permet l’ajout et la suppression d’actifs numériques.

Ce projet a été réalisé dans le cadre du module **Web3 – HETIC**, pour la validation du **Bloc 3 : Développer une solution digitale**.

---

## Fonctionnalités principales

- Inscription et authentification des utilisateurs
- Connexion sécurisée via JSON Web Token (JWT)
- Accès protégé au tableau de bord
- Ajout d’actifs crypto à un portefeuille
- Suppression d’actifs
- Calcul automatique de la valeur totale du portefeuille
- Données isolées par utilisateur

---

## Technologies utilisées

### Frontend
- Next.js
- React
- TypeScript

### Backend
- FastAPI
- Python

### Base de données
- PostgreSQL

### Sécurité
- Hashage des mots de passe (bcrypt)
- Authentification JWT
- Protection des routes sensibles

---

## Architecture du projet

crypto-portfolio/
├── backend/
│ ├── app/
│ │ ├── routes/
│ │ │ ├── auth.py
│ │ │ └── portfolio.py
│ │ ├── auth.py
│ │ ├── database.py
│ │ ├── models.py
│ │ ├── schemas.py
│ │ └── main.py
│ └── requirements.txt
│
├── frontend/
│ ├── app/
│ │ ├── login/
│ │ ├── register/
│ │ ├── dashboard/
│ │ └── services/
│ │ └── api.ts
│ └── package.json
│
└── README.md


---

## Installation et lancement

### Prérequis
- Node.js
- Python 3.10+
- PostgreSQL

---

### Backend

1. Se placer dans le dossier backend :
cd backend


2. Créer et activer un environnement virtuel :
python -m venv venv
source venv/bin/activate

(Sous Windows)
venv\Scripts\activate


3. Installer les dépendances :
pip install -r requirements.txt


4. Lancer le serveur :
uvicorn app.main:app --reload


Le backend est accessible à l’adresse :
http://localhost:8000


La documentation Swagger est disponible ici :
http://localhost:8000/docs


---

### Frontend

1. Se placer dans le dossier frontend :
cd frontend


2. Installer les dépendances :
npm install


3. Lancer le serveur de développement :
npm run dev


Le frontend est accessible à l’adresse :
http://localhost:3000


---

## Utilisation de l’application

1. Accéder à la page d’inscription :
/register


2. Créer un compte utilisateur

3. Se connecter via :
/login


4. Accéder au tableau de bord sécurisé :
/dashboard


5. Ajouter ou supprimer des actifs crypto depuis le dashboard

---

## Sécurité et authentification

- Les mots de passe sont stockés sous forme hashée
- Un token JWT est généré lors de la connexion
- Les routes du portefeuille sont protégées et accessibles uniquement aux utilisateurs authentifiés
- Chaque utilisateur ne peut accéder qu’à ses propres données

---

## Périmètre du projet

Ce projet correspond uniquement au **Bloc 3 – Développement informatique**.  
Les blocs 1 et 2 (documentation et gestion de projet) ne font pas partie du périmètre de cette livraison.

---

## Auteur

Joseph BAEGNE