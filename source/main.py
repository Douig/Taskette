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
                '\n'"3. Changer le statut d'une tâche",
                '\n'"4. Supprimer une tâche",
                '\n'"5. Quitter")
        if choix_menu.lower() == "2" or choix_menu.lower() == "5" or choix_menu.lower() == "quitter":
            print("A bientot !")
            break
except ValueError:
    print("Erreur")