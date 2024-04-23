# Chatbot AI Local

Ce projet est une AI local conçu pour fournir une expérience de conversation interactive. Il utilise LM Studio comme environnement de développement et un modèle de langage de grande taille (LLM) pour générer des réponses aux requêtes de l'utilisateur.

## Prérequis

Avant de lancer le projet, assurez-vous d'avoir les éléments suivants installés :

- LM Studio : Disponible sur [site officiel de LM Studio](https://lmstudio.ai/)
- Un modèle de langage (LLM) : Nous recommandons le téléchargement de Mistral instruct v0 1 7B Q4_K_M, disponible sur LM Studio.
- Local Inference Server : Assurez-vous que le serveur d'inférence local est en cours d'exécution pour permettre au chatbot de fonctionner correctement.

## Installation

1. Clonez ce dépôt GitHub sur votre machine locale :

    ```bash
    git clone https://github.com/goumix/chatbot-ai-local.git
    ```

2. Téléchargez toutes les dépendances nécessaires en exécutant la commande suivante :

    ```bash
    pip install streamlit
    pip install openai
    ```

## Utilisation

Une fois que vous avez installé les prérequis et téléchargé les dépendances du projet, vous pouvez lancer le chatbot AI local en suivant ces étapes :

1. Lancez LM Studio sur votre machine.
2. Chargez le modèle de langage (LLM) téléchargé (Mistral instruct v0 1 7B Q4_K_M).
3. Assurez-vous que le serveur d'inférence local est en cours d'exécution.
4. Ouvrez un terminal dans le répertoire du projet cloné.
5. Exécutez la commande suivante pour démarrer l'interface du chatbot :

    ```bash
    streamlit run interface.py
    ```

6. Une fois que l'interface est lancée, vous pouvez commencer à interagir avec le chatbot en saisissant vos requêtes dans la zone de texte prévue à cet effet.
