# Fichiers de données

La version portfolio n’inclut pas les classeurs métier réels afin d’éviter la publication accidentelle de données personnelles ou opérationnelles.

## `Base_de_donnees.xlsx`

Fichier utilisé comme base clients et comme support de facturation trimestrielle.

Le code fait référence aux colonnes suivantes :

```text
Nom
Prénom
Adresse
Montant_trimestre_1
Nb_courses_trimestre_1
Montant_trimestre_2
Nb_courses_trimestre_2
Montant_trimestre_3
Nb_courses_trimestre_3
Montant_trimestre_4
Nb_courses_trimestre_4
```

Les colonnes de nom et prénom sont normalisées lors de certaines recherches.

## `Récapitulatif_Courses.xlsx`

Fichier créé ou complété par l’application lors des réservations.

Le code utilise la structure suivante :

| Colonne | Contenu |
| --- | --- |
| A | ID Google Calendar — colonne masquée |
| B | Identifiant visible de la course |
| C | Date |
| D | Horaire |
| E | Nom |
| F | Prénom |
| G | Adresse Départ |
| H | Adresse Arrivée |
| I | Type Trajet |
| J | Montant |
| K | Chauffeur |

## Publication GitHub

Ces deux fichiers sont exclus par `.gitignore`. Pour une démonstration publique, utiliser uniquement des données fictives et anonymisées.
