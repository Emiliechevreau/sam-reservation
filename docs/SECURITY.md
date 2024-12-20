# Sécurité

## Fichiers exclus de la version portfolio

Le ZIP source contenait des fichiers d’authentification Google réels. Ils ne sont pas redistribués dans cette version :

```text
credentials.json
token.json
service-account.json
```

Les fichiers Excel métier d’origine sont également exclus car ils sont susceptibles de contenir des données personnelles ou opérationnelles.

## Action recommandée avant publication

Si les secrets présents dans le ZIP source ont déjà été envoyés dans un dépôt public, partagés avec des tiers ou stockés dans un emplacement non maîtrisé, les considérer comme compromis et les révoquer / régénérer depuis Google Cloud et le compte Google concerné.

## Points à durcir pour une version de production

Sans modifier le code d’origine, l’audit met en évidence plusieurs éléments qui devraient être traités lors d’une future refonte :

- identifiants de connexion codés en dur ;
- clé de session Flask codée en dur ;
- configuration des calendriers codée en dur ;
- secrets OAuth stockés sous forme de fichiers locaux ;
- absence de séparation entre configuration, données et code ;
- stockage métier Excel non adapté à des accès concurrents importants ;
- absence de politique d’autorisation fine par rôle ;
- absence de tests automatisés de sécurité et de non-régression.

## Bonnes pratiques Git

Avant chaque push :

```bash
git status
git diff --cached
```

Vérifier qu’aucun fichier de credentials, token, clé privée ou fichier client réel n’est inclus dans le commit.
