# On importe les fonctions de nos autres fichiers
from storage import charger_taches, sauvegarder_taches
from fonctions import creer_tache, trouver_tache_par_id
from utils import date_tache

# On dit au programme où trouver le fichier JSON.
# ATTENTION: Il faut lancer le script depuis le dossier "Taskette" !
FICHIER_TACHES = "data/tasks.json"

print("Bonjour et bienvenue dans Taskette !")
print("------------------------------------")

# On charge les tâches qui existent déjà
taches = charger_taches(FICHIER_TACHES)
print(f"Vous avez {len(taches)} tâche(s) en cours.")
print("Tapez 'menu' pour voir les options.")
print("------------------------------------")

# Notre variable qui contrôle si le programme doit tourner
programme_en_cours = True

# Tant que cette variable est Vraie, la boucle continue
while programme_en_cours:
    
    # On demande à l'utilisateur ce qu'il veut faire
    choix_menu = input("Votre choix : ")
    
    # On vérifie son choix
    
    if choix_menu == "menu":
        print("\n------ MENU TASKETTE ------")
        print("1. Lister les tâches")
        print("2. Ajouter une tâche")
        print("3. Modifier le statut d'une tâche")
        print("4. Supprimer une tâche")
        print("5. Quitter")
        print("---------------------------\n")

    # Si l'utilisateur tape 5 OU "quitter"
    elif choix_menu == "5" or choix_menu == "quitter":
        print("À bientôt !")
        # On met la variable à Faux, la boucle va s'arrêter
        programme_en_cours = False

    # Si l'utilisateur tape 1
    elif choix_menu == "1":
        print("\n--- Voici la liste de vos tâches ---")
        # Si la longueur de la liste est 0
        if len(taches) == 0:
            print("-> Aucune tâche pour le moment.")
        else:
            # On fait une boucle pour afficher chaque tâche
            for t in taches:
                print(f"-> ID {t['id']}: {t['titre']} (Statut: {t['statut']})")
        print("-" * 36 + "\n")

    # Si l'utilisateur tape 2
    elif choix_menu == "2":
        titre_tache = input("Quel est le titre de la nouvelle tâche ? ")
        try:
            # On essaie de créer la tâche
            nouvelle_tache = creer_tache(taches, titre_tache)
            # Si ça marche, on sauvegarde !
            sauvegarder_taches(taches, FICHIER_TACHES)
            print(f"Tâche '{nouvelle_tache['titre']}' ajoutée avec succès !")
        except ValueError as e:
            # Si 'creer_tache' nous a renvoyé une erreur (titre vide)
            print(f"Erreur : {e}")
        print("-" * 25 + "\n")

    # Si l'utilisateur tape 3
    elif choix_menu == "3":
        id_str = input("Entrez l'ID de la tâche à modifier : ")
        
        try:
            # On essaie de transformer le texte en nombre
            id_num = int(id_str)
        except ValueError:
            # Si ça rate (l'utilisateur a tapé "abc" par exemple)
            print("Erreur : Vous devez taper un nombre.")
            continue # 'continue' repart au début de la boucle while

        # On cherche la tâche avec ce numéro
        tache_trouvee = trouver_tache_par_id(taches, id_num)

        # Si notre fonction a trouvé la tâche
        if tache_trouvee:
            nouveau_statut = input(f"Entrez le nouveau statut pour '{tache_trouvee['titre']}' : ")
            
            # On met à jour le dictionnaire
            tache_trouvee['statut'] = nouveau_statut
            tache_trouvee['maj_le'] = date_tache() # On met à jour la date
            
            # On sauvegarde les changements
            sauvegarder_taches(taches, FICHIER_TACHES)
            print("Statut de la tâche mis à jour !")
        else:
            # Si la fonction n'a rien trouvé
            print(f"Erreur : Aucune tâche trouvée avec l'ID {id_num}.")
        print("-" * 25 + "\n")

    # Si l'utilisateur tape 4
    elif choix_menu == "4":
        id_str = input("Entrez l'ID de la tâche à supprimer : ")
        
        try:
            # On essaie de transformer le texte en nombre
            id_num = int(id_str)
        except ValueError:
            print("Erreur : Vous devez taper un nombre.")
            continue # On repart au début de la boucle

        # On cherche la tâche avec ce numéro
        tache_a_supprimer = trouver_tache_par_id(taches, id_num)

        # Si on a trouvé la tâche
        if tache_a_supprimer:
            # On demande confirmation
            confirmation = input(f"Voulez-vous vraiment supprimer '{tache_a_supprimer['titre']}' ? (oui/non) ")
            
            if confirmation == 'oui':
                # La façon la plus simple de supprimer un élément d'une liste
                taches.remove(tache_a_supprimer)
                
                # On sauvegarde la liste (qui a maintenant une tâche en moins)
                sauvegarder_taches(taches, FICHIER_TACHES)
                print("Tâche supprimée avec succès !")
            else:
                print("Suppression annulée.")
        else:
            # Si la fonction n'a rien trouvé
            print(f"Erreur : Aucune tâche trouvée avec l'ID {id_num}.")
        print("-" * 25 + "\n")

    # Si l'utilisateur tape n'importe quoi d'autre
    else:
        print("Choix non valide, veuillez réessayer. Tapez 'menu' pour voir les options.")