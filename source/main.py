from fonctions import creer_tache

print("Bonjour et bienvenue dans Taskette !")
print("1. Menu")
print("2. Quitter")

selection = ("(1/2)")

try:
    while selection != "2":
        choix_menu = input("")
        
        if choix_menu.lower() == "1" or choix_menu.lower() == "menu":
            print("1. Lister les tâches",
                '\n'"2. Ajouter une tâche",
                '\n'"3. Modifier une tâche",
                '\n'"4. Supprimer une tâche",
                '\n'"5. Quitter")
        if choix_menu.lower() == "2" or choix_menu.lower() == "5" or choix_menu.lower() == "quitter":
            print("A bientot !")
            break
        if choix_menu.lower() == "1" or choix_menu.lower() == "lister les tâches":
            print("Voici la liste de vos tâches :")
        if choix_menu.lower() == "2" or choix_menu.lower() == "ajouter une tâche":
            print("Ajouter une tâche")
        if choix_menu.lower() == "3" or choix_menu.lower() == "modifier une tâche":
            print("Modifier une tâche")
        if choix_menu.lower() == "4" or choix_menu.lower() == "supprimer une tâche":
            print("Supprimer une tâche")
except ValueError:
    print("Erreur")
