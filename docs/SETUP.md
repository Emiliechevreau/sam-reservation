# Installation et configuration

Ce guide complète le démarrage rapide du `README.md`.

## Prérequis

- Python 3 récent ;
- `pip` ;
- un navigateur web ;
- pour les fonctionnalités métier complètes : les fichiers Excel attendus par l'application ;
- pour la synchronisation : un projet Google Cloud avec Google Calendar API activée.

## Installation depuis un clone GitHub

```bash
git clone <URL_DU_DEPOT_GITHUB>
cd sam-reservation-portfolio
python -m venv .venv
```

Activer ensuite l'environnement :

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Puis installer les dépendances :

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Lancer les pages web

Les fichiers HTML sont des templates rendus par Flask. Il ne faut donc pas ouvrir directement `templates/*.html` dans le navigateur.

Démarrer le serveur :

```bash
python app.py
```

Ouvrir ensuite :

```text
http://127.0.0.1:5000
```

Identifiants de démonstration définis dans la version actuelle :

```text
Utilisateur : admin
Mot de passe : password123
```

Le tableau de bord permet ensuite de naviguer vers les écrans de réservation, de résumé et d'annulation.

## Données Excel

Pour exécuter les fonctions qui lisent ou écrivent les données métier, ajouter à la racine :

```text
Base_de_donnees.xlsx
Récapitulatif_Courses.xlsx
```

Voir [`DATA_FILES.md`](DATA_FILES.md) pour les colonnes utilisées par le code.

## OAuth Google Calendar

Créer des identifiants OAuth dans Google Cloud Console pour une **application de bureau**, puis télécharger le JSON associé.

Le fichier doit être placé ici :

```text
sam-reservation-portfolio/credentials.json
```

Le dépôt contient `credentials.example.json` uniquement pour illustrer la structure. Ne jamais committer de secrets réels.

Lors du premier flux d'authentification, `token.json` est généré automatiquement. Il est ignoré par Git.

## Utilitaire Calendar

Pour afficher les événements à venir des calendriers configurés :

```bash
python main.py
```

## Arrêter Flask

Dans le terminal qui exécute l'application :

```text
Ctrl + C
```

## Dépannage

### La page HTML ne s'ouvre pas

Vérifier que `python app.py` est toujours en cours d'exécution, puis utiliser `http://127.0.0.1:5000` au lieu d'ouvrir directement un fichier du dossier `templates/`.

### `credentials.json` introuvable

Vérifier que le fichier OAuth porte exactement ce nom et se trouve à la racine.

### Fichier Excel introuvable

Vérifier l'orthographe exacte des deux fichiers attendus par le code, notamment l'accent dans `Récapitulatif_Courses.xlsx`.

### Erreur Google Calendar

Vérifier :

- que Google Calendar API est activée ;
- que les autorisations OAuth ont été accordées ;
- que le compte authentifié a accès aux calendriers configurés ;
- que `token.json` correspond toujours au projet OAuth utilisé.
