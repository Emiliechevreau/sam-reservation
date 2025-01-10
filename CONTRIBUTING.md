# Contribution

## Objectif

Conserver un historique clair et éviter l’introduction de secrets ou de données personnelles dans le dépôt.

## Workflow recommandé

1. Créer une branche dédiée.
2. Installer les dépendances dans un environnement virtuel.
3. Utiliser uniquement des données fictives pour le développement partagé.
4. Vérifier `git diff` et `git status` avant tout commit.
5. Documenter les changements fonctionnels dans la pull request.

## Conventions

- Python : indentation de 4 espaces.
- HTML / YAML / Markdown : indentation de 2 espaces.
- Ne jamais committer `credentials.json`, `token.json`, `service-account.json` ou des classeurs contenant des données réelles.
- Éviter de mélanger refactor structurel et modification fonctionnelle dans le même commit.

## Évolutions suggérées

Une future refonte pourrait introduire :

- un package `src/` ;
- une configuration par variables d’environnement ;
- une vraie couche de persistance ;
- des tests unitaires et d’intégration ;
- une authentification dédiée ;
- une gestion centralisée des secrets.

Ces changements nécessiteraient toutefois de modifier le code applicatif et ne font pas partie de la présente version portfolio.
