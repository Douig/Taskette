# On importe 'json' pour que Python comprenne comment
# transformer nos listes en texte et inversement.
import json

def charger_taches(fichier):
    """
    Essaie de lire le fichier JSON.
    S'il n'existe pas ou est vide, retourne une liste vide [].
    """
    try:
        # 'with open' est la façon propre d'ouvrir un fichier
        # 'r' veut dire "read" (lire)
        with open(fichier, 'r', encoding='utf-8') as f:
            # On demande à json de "charger" (load) le contenu du fichier
            return json.load(f)
    except:
        # S'il y a la moindre erreur (fichier pas trouvé, fichier vide...)
        # on ne panique pas et on retourne juste une liste vide.
        return []

def sauvegarder_taches(taches, fichier):
    """
    Écrit la liste complète des tâches dans le fichier JSON.
    """
    # 'w' veut dire "write" (écrire). ATTENTION: ça écrase l'ancien contenu.
    with open(fichier, 'w', encoding='utf-8') as f:
        # On demande à json de "jeter" (dump) nos données dans le fichier
        # indent=4 : C'est pour que le fichier soit joli et lisible
        # ensure_ascii=False : C'est TRÈS important pour que les accents
        # (comme "à" ou "é") soient bien enregistrés.
        json.dump(taches, f, indent=4, ensure_ascii=False)