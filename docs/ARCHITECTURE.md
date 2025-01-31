# Architecture

## Vue d'ensemble

L’application suit une architecture Flask simple, orientée vers un usage local :

```text
Navigateur
   │
   ▼
Flask / app.py
   ├── Templates Jinja / HTML
   ├── Base clients Excel
   ├── Récapitulatif des courses Excel
   └── Google Calendar API
```

## Composants

### `app.py`

Point d’entrée principal. Il regroupe :

- les routes Flask ;
- l’authentification de session ;
- la recherche client ;
- la tarification ;
- la réservation et l’annulation ;
- l’accès à Google Calendar ;
- les lectures et écritures Excel ;
- la mise en forme du récapitulatif de courses.

### `main.py`

Script autonome permettant d’interroger les calendriers Google configurés et d’afficher les prochains événements de chaque chauffeur.

### `templates/`

Contient les vues HTML utilisées par Flask :

| Fichier | Rôle |
| --- | --- |
| `login.html` | Connexion |
| `Page_accueil.html` | Tableau de bord |
| `formulaire.html` | Création d’une réservation |
| `validation.html` | Confirmation d’une réservation |
| `summary.html` | Résumé de facturation client |
| `annulation.html` | Recherche et annulation de courses |
| `client_non_trouve.html` | Gestion d’un client absent |
| `data.yaml` | Ressource conservée de la version d’origine |

## Flux de réservation

1. L’utilisateur saisit l’identité du client, les adresses, l’horaire, le type de trajet, la durée et le chauffeur.
2. Les noms sont normalisés et comparés à la base client avec RapidFuzz lorsque nécessaire.
3. Le prix est déterminé à partir du type de trajet.
4. Un événement est créé dans le calendrier Google du chauffeur.
5. La course est enregistrée dans le fichier récapitulatif.
6. Les compteurs et montants trimestriels du client sont mis à jour.

## Flux d’annulation

1. Recherche des courses selon le client et le mois.
2. Identification de la ligne Excel et de l’identifiant d’événement Calendar.
3. Déduction du montant dans la base client.
4. Suppression de l’événement Google Calendar.
5. Suppression de la ligne du récapitulatif et recalcul des identifiants visibles.

## Contraintes structurelles actuelles

Plusieurs ressources sont référencées avec des chemins relatifs depuis la racine. Une architecture `src/`, `data/` et `config/` serait pertinente dans une refonte future, mais elle exigerait des modifications de code. Elle n’est donc pas appliquée dans cette version portfolio.
