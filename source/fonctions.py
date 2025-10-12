import locale
from datetime import datetime

def date_tache():
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    valeur = datetime.now()
    temps = valeur.strftime("%d %B %Y à %Hh%M")
    return temps