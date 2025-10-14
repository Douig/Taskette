import json

def charger_taches(fichier: str) -> list:
    """
    Charge les tâches depuis un fichier JSON.
    Retourne une liste vide si le fichier n'existe pas ou est invalide.
    """
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si le fichier n'est pas trouvé ou s'il est vide/corrompu,
        # on commence avec une liste de tâches vide.
        return []

def sauvegarder_taches(taches: list, fichier: str):
    """Sauvegarde la liste complète des tâches dans un fichier JSON."""
    with open(fichier, 'w', encoding='utf-8') as f:
        # indent=4 pour que le fichier JSON soit lisible par un humain
        # ensure_ascii=False pour bien gérer les accents comme 'é', 'à', etc.
        json.dump(taches, f, indent=4, ensure_ascii=False)