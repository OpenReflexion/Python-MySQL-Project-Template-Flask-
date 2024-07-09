# Flask MySQL Project Template

Ce dépôt offre une architecture de base en Python pour des projets Flask avec MySQL, permettant un démarrage rapide. Inclut Docker, contrôleurs, modèles, routes et services. Adaptable pour d'autres structures API comme FastAPI et bien d'autres.

## Structure du Projet

```plaintext

├── LICENSE
├── docs                         # Documentation du projet
│   ├── example                  # Exemples de schémas Swagger
│   └── migration.md             # Documentation des migrations
├── migrations                   # Gestion des migrations de base de données avec Alembic
├── src                          # Code source de l'application
│   ├── config                   # Configuration de l'application
│   ├── controllers              # Contrôleurs pour gérer les logiques métiers des routes
│   ├── exception                # Gestion des exceptions personnalisées
│   ├── models                   # Définition des modèles de données SQLAlchemy
│   ├── repositories             # Repositories pour interagir avec la base de données
│   ├── routers                  # Définition des routes de l'application
│   ├── schemas                  # Schémas de validation des données
│   ├── services                 # Services pour encapsuler la logique métier
│   ├── templates                # Templates HTML (si nécessaire)
│   ├── utils                    # Utilitaires et fonctions auxiliaires
│   └── validators               # Validateurs de données
├── tests                        # Tests unitaires et d'intégration
└── var                          # Fichiers de log
    └── logs                     # Dossiers contenant les logs de développement
├── main.py                      # Point d'entrée principal de l'application
├── requirements.txt             # Liste des dépendances Python
│   ├── database.py
│   ├── jwt.py
│   ├── logging.py
│   ├── path_config.py
│   └── settings.py
│   ├── auth_controller.py
│   └── user_controller.py
│   └── exceptions.py
│   └── user_model.py
│   └── user_repository.py
│   ├── auth_router.py
│   └── user_router.py
│   └── auth_schemas.py
│   ├── auth_service.py
│   └── user_service.py
│   └── __init__.py

```


## Installation

### Prérequis

- Python 3.11
- MySQL
- Docker (optionnel pour déploiement via conteneur)

### Étapes d'installation

1. **Cloner le dépôt :**

    ```bash
    git clone https://github.com/OpenReflexion/Python-MySQL-Project-Template-Flask-.git
    cd Python-MySQL-Project-Template-Flask-
    ```

2. **Créer et activer un environnement virtuel :**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Pour Windows, utilisez `.venv\Scripts\activate`
    ```

3. **Installer les dépendances :**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurer les variables d'environnement :**

    Copiez le fichier `.env.example` en `.env` :

    ```bash
    cp .env.example .env
    ```

    Puis, modifiez le fichier `.env` pour y ajouter vos configurations spécifiques :

    ```env
    SECRET_KEY=votre_cle_secrete
    SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:password@localhost/db_name
    JWT_SECRET_KEY=votre_cle_secrete_jwt
    ```

5. **Initialiser la base de données :**

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Démarrage du Projet

1. **Lancer l'application :**

    ```bash
    flask run
    ```

2. **Accéder à l'application :**

    Ouvrez votre navigateur et allez à `http://127.0.0.1:5000`

## Gestion des Migrations

1. **Créer une nouvelle migration :**

    ```bash
    flask db migrate -m "Description de la migration"
    ```

2. **Appliquer les migrations :**

    ```bash
    flask db upgrade
    ```

## Notes

- N'oubliez pas de donner une étoile à ce dépôt si vous le trouvez utile !
- Vous êtes libre de faire évoluer ce projet comme vous le souhaitez.

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
