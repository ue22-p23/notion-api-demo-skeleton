# Notion API demo

Cette application de console Python permet de gérer des tâches stockées dans une base de données Notion. Utilisant prompt_toolkit pour une interaction utilisateur avancée et l'API Notion pour le stockage et la récupération des données, elle offre une solution pratique pour suivre l'avancement des projets ou des tâches directement depuis le terminal.

## Fonctionnalités

- Lister les tâches : Affiche toutes les tâches de la base de données Notion avec la possibilité de filtrer par statut.
- Afficher les détails d'une tâche : Montre des informations détaillées sur une tâche spécifique, y compris son contenu en format Markdown.
- Mettre à jour une tâche : Permet de modifier le statut ou d'autres propriétés d'une tâche spécifique.
- Ajouter du contenu à une tâche : Ajoute du texte dans le corps d'une tâche, en supportant différents types de blocs comme les paragraphes et les en-têtes.

## Prérequis

Avant d'utiliser l'application, assurez-vous d'avoir Python 3.6 ou une version ultérieure installée sur votre système. Vous aurez également besoin de :

- Un compte Notion et une intégration API configurée pour accéder à votre base de données Notion.
- Le token d'accès de l'API et l'ID de la base de données Notion à laquelle l'application accèdera.

Pour la structure de base de donnée, il vous suffit de dupliquer la [mienne](https://bmarchand.notion.site/04620d6c67274d8e96211ddc738acf76?v=31bcb2e38fa242cfbc8eb9c51eca6108)

## Installation

Installez les dépendances nécessaires :

```
pip install -r requirements.txt
```

Les dépendances incluent `requests`, `prompt_toolkit`, `markdown`, et `rich`.

## Configuration

Créez un fichier .env dans le répertoire racine de l'application et ajoutez-y votre token d'accès de l'API Notion et l'ID de votre base de données :

```
NOTION_TOKEN=votre_token_d'API
DATABASE_ID=votre_id_de_base_de_données
```

## Utilisation

Pour lancer l'application, exécutez :

```
python main.py
```

Suivez les instructions à l'écran pour interagir avec votre base de données Notion.
