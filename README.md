# SAM — Application de réservation et gestion de courses

Application web Flask conçue pour centraliser la **réservation**, le **suivi**, l’**annulation** et la **facturation** de courses, avec synchronisation des créneaux dans **Google Calendar** et stockage opérationnel dans des fichiers Excel.

> Version portfolio : le code applicatif d’origine est conservé tel quel. Le dépôt a uniquement été nettoyé et documenté pour une publication GitHub plus lisible et plus sûre.

## Aperçu

Le projet propose une interface web permettant de :

- authentifier un utilisateur avant l’accès au tableau de bord ;
- rechercher un client dans une base Excel avec tolérance aux variations de saisie ;
- créer une réservation et calculer son montant selon le type de trajet ;
- associer une course à un chauffeur et créer l’événement correspondant dans Google Calendar ;
- enregistrer les courses dans un récapitulatif Excel ;
- consulter un résumé de facturation par client et par trimestre ;
- rechercher et annuler une réservation ;
- répercuter l’annulation dans Google Calendar et dans les données de facturation.

## Stack technique

| Domaine | Technologies |
| --- | --- |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript, Jinja |
| Données | pandas, openpyxl, Excel `.xlsx` |
| Matching | RapidFuzz |
| Intégration | Google Calendar API, OAuth 2.0 |
| Exécution | Application Flask locale |

## Architecture du dépôt

```text
sam-reservation-portfolio/
├── app.py                     # Application Flask principale
├── main.py                    # Script utilitaire Google Calendar
├── templates/                 # Pages HTML / Jinja
├── images/                    # Ressources graphiques d'origine
├── docs/
│   ├── ARCHITECTURE.md        # Flux fonctionnels et composants
│   ├── DATA_FILES.md          # Structure attendue des fichiers Excel
│   ├── SECURITY.md            # Précautions avant publication / déploiement
│   └── SETUP.md               # Installation détaillée
├── credentials.example.json   # Exemple OAuth sans secret
├── requirements.txt           # Dépendances Python
├── .gitignore                 # Secrets, données locales et fichiers temporaires
├── .editorconfig              # Conventions d'édition
└── CONTRIBUTING.md            # Règles de contribution
```

### Pourquoi `app.py` et `templates/` restent à la racine ?

Le code utilise actuellement plusieurs chemins relatifs (`credentials.json`, `token.json`, `Base_de_donnees.xlsx`, `Récapitulatif_Courses.xlsx`) et la convention Flask standard pour `templates/`. Les déplacer sans modifier le code pourrait casser l’exécution. La version portfolio privilégie donc une **réorganisation non destructive**.

## Installation rapide

### 1. Créer un environnement virtuel

```bash
python -m venv .venv
```

Activation :

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Configurer Google Calendar

1. Créer un projet dans Google Cloud Console.
2. Activer **Google Calendar API**.
3. Créer des identifiants OAuth de type application de bureau.
4. Télécharger le fichier JSON et le placer à la racine sous le nom `credentials.json`.
5. Ne jamais committer ce fichier.

Un modèle est fourni dans `credentials.example.json`.

Lors du premier lancement nécessitant l’API Google, l’application ouvre le flux OAuth puis génère localement `token.json`.

### 4. Ajouter les fichiers de données locaux

Le code attend à la racine :

```text
Base_de_donnees.xlsx
Récapitulatif_Courses.xlsx
```

Ces fichiers ne sont volontairement pas inclus dans la version portfolio car ils peuvent contenir des données personnelles ou opérationnelles. Leur structure est détaillée dans [`docs/DATA_FILES.md`](docs/DATA_FILES.md).

### 5. Lancer l’application

```bash
python app.py
```

Puis ouvrir l’adresse Flask affichée dans le terminal.

## Flux principal

```text
Connexion
   ↓
Tableau de bord
   ├── Nouvelle réservation
   │      ↓
   │  Recherche client → Calcul tarif → Google Calendar → Excel
   │
   ├── Résumé client
   │      ↓
   │  Lecture base Excel → synthèse trimestrielle
   │
   └── Annulation
          ↓
      Recherche course → suppression Calendar → mise à jour Excel
```

## Points techniques mis en œuvre

- routes Flask avec rendu Jinja et réponses JSON ;
- gestion de session pour le contrôle d’accès ;
- lecture et écriture de classeurs Excel ;
- normalisation des noms et suppression des accents ;
- fuzzy matching avec `RapidFuzz` ;
- création et suppression d’événements Google Calendar ;
- logique de facturation trimestrielle ;
- gestion multi-chauffeurs via plusieurs calendriers ;
- adaptation de l’ouverture du fichier Excel selon Windows, macOS ou Linux.

## Sécurité et limites

Cette application correspond à un projet applicatif / prototype et nécessite plusieurs durcissements avant un déploiement de production :

- identifiants de connexion actuellement définis dans le code ;
- clé Flask de session définie dans le code ;
- identifiants de calendriers présents dans le code ;
- stockage Excel local plutôt qu’une base de données transactionnelle ;
- gestion des secrets OAuth prévue pour une exécution locale ;
- absence de suite de tests automatisés dans la version d’origine.

Ces éléments sont documentés sans être corrigés ici afin de respecter la contrainte : **aucune modification du code applicatif**. Voir [`docs/SECURITY.md`](docs/SECURITY.md).

## Documentation

- [Installation détaillée](docs/SETUP.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Fichiers de données](docs/DATA_FILES.md)
- [Sécurité](docs/SECURITY.md)
- [Contribution](CONTRIBUTING.md)

## Contexte portfolio

Ce dépôt met notamment en avant :

- la conception d’un workflow métier de réservation de bout en bout ;
- l’intégration d’une API tierce via OAuth 2.0 ;
- la manipulation de données Excel avec Python ;
- le traitement de saisies utilisateurs avec fuzzy matching ;
- la construction d’une application web Flask multi-écrans ;
- la synchronisation entre interface web, données locales et calendrier externe.

## Licence

Aucune licence n’est ajoutée automatiquement à cette version. Avant de publier le dépôt, ajouter la licence correspondant réellement aux droits du projet et aux éventuels contributeurs.
