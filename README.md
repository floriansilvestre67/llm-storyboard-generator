# 🎬 LLM-driven Storyboard Generator

## 📌 Présentation du Projet
Ce projet est un système **End-to-End** qui transforme un script court (un paragraphe) en un storyboard visuel cohérent. L'objectif est d'automatiser le processus créatif : un LLM analyse le récit pour en extraire des scènes clés, lesquelles sont ensuite illustrées par un modèle de génération d'images.

Le projet est conçu de manière **hybride** :
1.  **Mode Local (Priorité) :** Utilisation de PyTorch, Ollama (Llama 3) et Stable Diffusion pour une exécution 100% privée.
2.  **Mode Cloud (Fallback) :** Utilisation de l'API Google Gemini (Pro & Imagen) en cas de limitations matérielles.

---

## 🏗️ Architecture du Système



1.  **Input :** **Script** textuel (paragraphe).
2.  **LLM Parser :** Extraction des personnages, décors et actions au format JSON.
3.  **Image Engine :** Génération des visuels via des modèles de diffusion.
4.  **UI :** Interface de visualisation et d'exportation.

---

## 👥 Répartition de l'Équipe

| Membre | Rôle | Responsabilités Techniques |
| :--- | :--- | :--- |
| **Membre A** | **NLP Engineer** | Intégration d'Ollama/Llama 3, Prompt Engineering pour le parsing JSON, fallback API Gemini. |
| **Membre B** | **Vision Expert** | Implémentation de SDXL avec **PyTorch**, optimisation de la VRAM (quantification), cohérence de style. |
| **Membre C** | **Fullstack AI** | Développement de l'interface **Streamlit**, orchestration du pipeline, gestion des exports images/PDF. |

---

## 🛠️ Stack Technique

*   **Langage :** Python 3.11+
*   **Deep Learning :** PyTorch, Hugging Face `diffusers` & `transformers`.
*   **LLM :** Ollama (Llama 3.2) / Google Gemini API.
*   **Génération d'images :** Stable Diffusion XL (SDXL) / Imagen 4.
*   **Interface :** Streamlit.

---

## 🚀 Installation

### 1. Cloner le dépôt
```bash
git clone [https://github.com/florianSilvestre/llm-storyboard-generator.git](https://github.com/florianSilvestre/llm-storyboard-generator.git)
cd llm-storyboard-generator
```

## 🌿 Convention de Contribution (Git Flow)
Pour garantir la stabilité du projet, nous utilisons des branches. La branche main doit toujours rester fonctionnelle.

Créer une nouvelle fonctionnalité
```bash
git checkout main
git pull origin main
git checkout -b feature-nom-de-votre-tache
Sauvegarder et partager son travail
```
```bash
git add .
git commit -m "Description claire de la modification"
git push origin feature-nom-de-votre-tache
```
Fusionner (Merge)
Ouvrez une Pull Request sur GitHub.

Demandez une revue aux deux autres membres de l'équipe.

Après validation, fusionnez la branche dans main.