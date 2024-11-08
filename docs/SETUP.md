# Installation et configuration

## Prérequis

- Python 3 récent ;
- `pip` ;
- un navigateur web ;
- un projet Google Cloud avec Google Calendar API activée ;
- les fichiers Excel métier attendus par l’application.

## Installation

```bash
git clone <URL_DU_REPOSITORY>
cd sam-reservation-portfolio
python -m venv .venv
```

Activation de l’environnement :

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Puis :

```bash
pip install -r requirements.txt
```

## OAuth Google Calendar

Créer des identifiants OAuth dans Google Cloud Console pour une application de bureau puis télécharger le JSON associé.

Le fichier doit être placé ici :

```text
sam-reservation-portfolio/credentials.json
```

Le dépôt contient `credentials.example.json` uniquement pour illustrer la structure. Ne pas y placer de secret réel avant de le committer.

Au premier flux d’authentification, `token.json` est généré automatiquement. Il est ignoré par Git.

## Données Excel

Ajouter à la racine :

```text
Base_de_donnees.xlsx
Récapitulatif_Courses.xlsx
```

Voir `DATA_FILES.md` pour les colonnes utilisées par le code.

## Lancement

```bash
python app.py
```

## Utilitaire Calendar

Pour afficher les événements à venir des calendriers configurés :

```bash
python main.py
```

## Dépannage

### `credentials.json` introuvable

Vérifier que le fichier OAuth porte exactement ce nom et se trouve à la racine.

### Fichier Excel introuvable

Vérifier l’orthographe exacte des deux fichiers attendus par le code, notamment l’accent dans `Récapitulatif_Courses.xlsx`.

### Erreur Google Calendar

Vérifier :

- que l’API Google Calendar est activée ;
- que les scopes OAuth ont été autorisés ;
- que le compte authentifié a accès aux calendriers configurés ;
- que `token.json` correspond toujours au projet OAuth utilisé.
