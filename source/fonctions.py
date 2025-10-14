from models import tache
from utils import date_tache

def _prochain_id(taches: list) -> int:
    """Retourne l'ID suivant (1 si la liste est vide)."""
    return max((t["id"] for t in taches), default=0) + 1

def creer_tache(taches: list, titre: str) -> dict:
    """
    Crée une nouvelle tâche et l'ajoute à la liste.
    - titre : nom de la tâche (non vide)
    - ajoute les champs 'id', 'statut', 'cree_le', 'maj_le'
    - retourne la tâche créée (dict)
    """
    titre = (titre or "").strip()
    if not titre:
        raise ValueError("Le titre de la tâche ne peut pas être vide.")

    # On récupère la date lisible grâce à ta fonction
    date_actuelle = date_tache()

    tache = {
        "id": _prochain_id(taches),
        "titre": titre,
        "statut": "à faire",
        "cree_le": date_actuelle,
        "maj_le": date_actuelle
    }

    taches.append(tache)
    return tache

# Cette fonction cherche une tâche par son ID et nous la retourne.
def trouver_tache_par_id(taches: list, id_tache: int) -> dict:
    # On parcourt chaque tâche dans notre liste de tâches
    for tache in taches:
        # Si l'ID de la tâche qu'on regarde est celui qu'on cherche...
        if tache["id"] == id_tache:
            # ... alors on a trouvé ! On retourne cette tâche.
            return tache
    
    # Si on a fini la boucle sans rien trouver, on retourne "Rien" (None).
    return None