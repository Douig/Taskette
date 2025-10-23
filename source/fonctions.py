# On a besoin de notre fonction de date pour la création
from utils import date_tache

def _prochain_id(taches):
    """
    Trouve le plus grand ID dans la liste et retourne le numéro d'après.
    Commence à 1 si la liste est vide.
    """
    # Si la liste de tâches est vide
    if len(taches) == 0:
        # Le premier ID sera 1
        return 1
    
    # Sinon, on doit trouver le plus grand ID
    id_max = 0 # On commence à 0
    # On fait une boucle sur chaque 'tache' dans notre liste 'taches'
    for tache in taches:
        # Si l'ID de la tâche qu'on regarde est plus grand que notre max
        if tache["id"] > id_max:
            # Alors ce devient notre nouveau max
            id_max = tache["id"]
            
    # On retourne le plus grand ID trouvé + 1
    return id_max + 1

def creer_tache(taches, titre):
    """
    Crée une nouvelle tâche (un dictionnaire) et l'ajoute à la liste.
    """
    
    # .strip() enlève les espaces au début et à la fin
    # ex: "   faire les courses   " devient "faire les courses"
    titre = titre.strip()
    
    # Si le titre est vide après avoir enlevé les espaces
    if titre == "":
        # On lève une erreur pour que le 'main.py' soit au courant
        raise ValueError("Le titre ne peut pas être vide.")

    # On récupère la date lisible
    date_actuelle = date_tache()

    # On crée notre dictionnaire "tache"
    tache = {
        "id": _prochain_id(taches),
        "titre": titre,
        "statut": "à faire",
        "cree_le": date_actuelle,
        "maj_le": date_actuelle
    }

    # On ajoute ce nouveau dictionnaire à notre liste principale
    taches.append(tache)
    
    # On retourne la tâche qu'on vient de créer
    return tache

def trouver_tache_par_id(taches, id_tache):
    """
    Cherche une tâche par son ID dans la liste.
    Retourne la tâche (dictionnaire) si on la trouve.
    Retourne None (Rien) si on ne la trouve pas.
    """
    # On parcourt chaque tâche dans notre liste
    for tache in taches:
        # Si l'ID de la tâche qu'on regarde est celui qu'on cherche
        if tache["id"] == id_tache:
            # On retourne la tâche (le dictionnaire)
            return tache
    
    # Si on a fini la boucle sans rien trouver, on retourne "Rien"
    return None