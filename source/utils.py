# source/utils.py

from datetime import datetime

def date_tache():
    """
    Retourne la date et l'heure actuelles dans un format numérique fiable (YYYY-MM-DD à HHhMM).
    Cette méthode ne dépend pas de la configuration de langue du système.
    """
    valeur = datetime.now()
    # On utilise un format qui marche sur tous les systèmes : %Y-%m-%d
    temps = valeur.strftime("%Y-%m-%d à %Hh%M")
    return temps