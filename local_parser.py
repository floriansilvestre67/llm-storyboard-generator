import requests
import json
import os

def parse_script_local(script_text):
    # L'URL par défaut où Ollama écoute
    url = "http://localhost:11434/api/generate"
    
    # Le prompte système pour forcer le JSON
    prompt = f"""
    Tu es un assistant de storyboard professionnel. Analyse le script suivant et décompose-le en scènes.
    
    INSTRUCTIONS SPÉCIALES :
    1. Crée d'abord une description physique stable pour chaque personnage dans 'characters_description' (âge, vêtements, traits distinctifs).
    2. Utilise ces descriptions dans chaque 'visual_description' des scènes pour garantir la cohérence visuelle.
    3. Réponds UNIQUEMENT avec un objet JSON strict.

    Structure JSON attendue :
    {{
      "titre": "Titre de l'histoire",
      "characters_description": [
        "Nom du perso : description physique détaillée"
      ],
      "storyboard": [
        {{
          "scene_number": 1,
          "visual_description": "description détaillée incluant le décor, l'action et le rappel du physique des persos",
          "characters": ["Nom des personnages présents"],
          "camera_angle": "type de plan "
        }}
      ]
    }}
    
    Script : {script_text}
    """

    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "format": "json", # Très important : force Ollama à sortir du JSON
        "stream": False   # On attend la réponse complète
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        # Extraction du texte de la réponse
        result_text = response.json().get('response', '{}')
        return json.loads(result_text)
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Ollama n'est pas lancé ou erreur : {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Le modèle n'a pas renvoyé un JSON valide."}


def save_to_json(data):
    
    output_dir = "./output/prompt_storyboard"
    
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Dossier créé : {output_dir}")

   
    raw_title = data.get("titre") or data.get("Titre") or "histoire_inconnue"
    
    # Nettoyage du nom de fichier : minuscules, remplace espaces par _, retire ponctuation simple
    clean_title = "".join(c for c in raw_title if c.isalnum() or c==' ').strip().replace(" ", "_").lower()
    filename = f"{clean_title}.json"
    filepath = os.path.join(output_dir, filename)

    # 4. Écriture du fichier
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ Fichier sauvegardé sous : {filepath}")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")

# --- TEST ---
if __name__ == "__main__":
    test_text = "Un pirate découvre un coffre sur une plage déserte. Soudain, un squelette sort du sable."
    data = parse_script_local(test_text)
    print(json.dumps(data, indent=4, ensure_ascii=False))
    
    # Sauvegarde automatique
    if "error" not in data:
        save_to_json(data)
    else:
        print("⚠️ Sauvegarde annulée suite à une erreur de parsing.")