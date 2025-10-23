# On a juste besoin de 'datetime' pour connaître la date et l'heure
from datetime import datetime

# On définit une fonction (un bloc de code) qu'on pourra appeler
def date_tache():
    """
    Retourne la date et l'heure actuelles dans un format simple.
    Exemple: "2025-10-23 à 14h30"
    """
    
    # 1. On récupère la date et l'heure de MAINTENANT
    valeur = datetime.now()
    
    # 2. On la met en forme comme on veut
    # %Y = Année (ex: 2025)
    # %m = Mois (ex: 10)
    # %d = Jour (ex: 23)
    # %H = Heure (ex: 14)
    # %M = Minute (ex: 30)
    temps = valeur.strftime("%Y-%m-%d à %Hh%M")
    
    # 3. On retourne le texte
    return temps