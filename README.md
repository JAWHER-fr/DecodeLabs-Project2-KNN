### 2️⃣ Fichier `README.md` pour le Projet 2 (Classification KNN)
*À placer dans ton dépôt dédié au Projet 2 (`DecodeLabs-Project2-KNN`)*

```markdown
# Project 2: Supervised Learning - Data Classification

## Domain: Artificial Intelligence Track
**Developed by:** Dridi Jawher  
**Algorithm:** K-Nearest Neighbors (KNN)  
**Dataset:** Iris Plant Benchmark  

## System Architectural Design
Ce projet marque la transition d'un système à règles fixes vers l'apprentissage automatique supervisé (Supervised Learning). L'objectif est d'entraîner un modèle capable de classifier automatiquement des espèces de fleurs (Iris) en fonction de leurs mesures morphologiques, tout en respectant un pipeline d'ingénierie rigoureux.

### Pipeline de l'Architecture :
1. **Input Phase :** Chargement du jeu de données Iris (150 échantillons, 4 caractéristiques).
2. **Data Integrity (Split & Shuffle) :** Division stricte des données (80% pour l'entraînement, 20% pour le test) avec mélange aléatoire pour éliminer tout biais d'ordre.
3. **Gatekeeper Rule (Feature Scaling) :** Normalisation des données via `StandardScaler` (Moyenne = 0, Variance = 1) pour équilibrer le calcul des distances géométriques.
4. **Model Tuning :** Application de l'algorithme KNN avec un paramètre optimal fixé à `n_neighbors=5`.
5. **Output Evaluation :** Analyse de la précision du modèle à l'aide d'une matrice de confusion (Confusion Matrix) et du calcul du score Macro F1.

## Structure des Fichiers
* `project2.py` - Le code source de l'entraînement et de l'évaluation.
* `DecodeLabs_Project2_Dridi_Jawher.pdf` - Le rapport technique de classification.
* `README.md` - Documentation du projet.

## Instructions de Déploiement
Installez les dépendances nécessaires avant l'exécution :
```bash
pip install scikit-learn pandas
