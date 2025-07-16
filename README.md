
# 📚 Flashcard Generator

Un petit projet Python qui permet de générer et de tester des **flashcards** personnalisées à partir d’un sujet donné par l’utilisateur.

---

## 🚀 Fonctionnalités

- Génération automatique de flashcards basées sur un sujet.
- Mélange aléatoire des questions à chaque exécution.
- Quiz interactif en ligne de commande avec retour immédiat.
- Tests unitaires avec `pytest` pour vérifier les fonctions principales.

---

## 🛠️ Structure du projet

```

Flashcard/
├── project.py           # Script principal contenant le programme et les fonctions
├── test\_project.py      # Tests unitaires pour les fonctions personnalisées
├── requirements.txt     # Dépendances Python (vide ici, mais présent)
└── README.md            # Ce fichier

````

---

## ▶️ Utilisation

### 1. Cloner le dépôt ou télécharger les fichiers :
```bash
git clone
cd flashcard-generator
````

### 2. Lancer le programme :

```bash
python project.py
```

### 3. Exemple :

```
Welcome to the Flashcard Quiz!
Please enter a topic for your flashcards: python
What is python? <votre réponse>
Correct!
Why is python important? <votre réponse>
Incorrect! The correct answer is: It helps understand python better.
```

---

## 🧪 Lancer les tests

### Installer `pytest` :

```bash
python -m pip install --user pytest
```

### Exécuter les tests :

```bash
python -m pytest test_project.py
```

---

## 📦 Dépendances

Aucune dépendance externe requise pour le moment.

```txt
# requirements.txt
# (Vide)
```

---

## 📌 À venir (idées d’amélioration)

* Génération automatique de vraies questions avec ChatGPT ou une API.
* Enregistrement des scores utilisateur.
* Mode "révision" ou "test rapide".
* Interface graphique avec Tkinter ou version web avec Flask.

---

## 👤 Auteur

Projet réalisé par Jouneid

