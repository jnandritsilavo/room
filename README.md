# Système de Réservation de Salles Universitaires

## Description
Ce projet est une application web permettant aux étudiants et enseignants de réserver des salles dans une université. L'administrateur peut gérer les salles et superviser les réservations. L'application est construite avec **Flask** pour le backend et **HTML/CSS/Bootstrap** pour le frontend.

## Fonctionnalités
- ✅ Inscription et connexion des utilisateurs avec **JWT**
- ✅ Gestion des rôles : **Étudiant, Enseignant, Administrateur**
- ✅ Réservation de salles par date et heure
- ✅ Annulation des réservations
- ✅ Affichage des salles disponibles
- ✅ Interface simple et intuitive

## Technologies Utilisées
- **Backend** : Flask, Flask-JWT-Extended, Flask-SQLAlchemy, Flask-Bcrypt
- **Base de Données** : SQLite (peut être remplacée par MySQL)
- **Frontend** : HTML, CSS, Bootstrap
- **Versionnement** : Git, GitHub

## Installation
### 1. Cloner le dépôt
```sh
git clone https://github.com/jnandritsilavo/room.git
cd room
```

### 2. Créer un environnement virtuel et installer les dépendances
```sh
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Démarrer l’application
```sh
python app.py
```
L’application sera accessible à l’adresse : [http://127.0.0.1:5000](http://127.0.0.1:5000)

## API Endpoints
```plaintext
Méthode  | Endpoint    | Description
---------|------------|--------------------------------
POST     | /register  | Inscription d'un utilisateur
POST     | /login     | Connexion et obtention d'un token JWT
POST     | /reserve   | Réserver une salle (nécessite un token)
```

## Améliorations Futures
- 📩 Ajout des notifications par email
- ⚛️ Interface utilisateur plus avancée avec Vue.js/React
- 📅 Gestion complète des salles et des réservations

## Auteur
👨‍💻 Développé par **Jean Narivelo**

