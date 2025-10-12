import locale
from datetime import datetime
from models import tache

def date_tache():
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    valeur = datetime.now()
    temps = valeur.strftime("%d %B %Y à %Hh%M")
    return temps

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