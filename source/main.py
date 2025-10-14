import pathlib
from storage import charger_taches, sauvegarder_taches
# On importe les fonctions nécessaires
from fonctions import creer_tache, trouver_tache_par_id # <-- AJOUT
from utils import date_tache # <-- AJOUT

# On construit un chemin absolu et fiable vers le fichier de sauvegarde
CHEMIN_PROJET = pathlib.Path(__file__).parent.parent
FICHIER_TACHES = CHEMIN_PROJET / "data" / "tasks.json"

print("Bonjour et bienvenue dans Taskette !")
print("------------------------------------")

taches = charger_taches(FICHIER_TACHES)
print(f"Vous avez {len(taches)} tâche(s) en cours.")
print("Tapez 'menu' pour voir les options.")
print("------------------------------------")

programme_en_cours = True

try:
    while programme_en_cours:
        choix_menu = input("Votre choix : ")

        if choix_menu.lower() == "menu":
            print("\n------ MENU TASKETTE ------")
            print("1. Lister les tâches")
            print("2. Ajouter une tâche")
            print("3. Modifier le statut d'une tâche")
            print("4. Supprimer une tâche")
            print("5. Quitter")
            print("---------------------------\n")

        elif choix_menu.lower() == "5" or choix_menu.lower() == "quitter":
            print("À bientôt !")
            programme_en_cours = False

        elif choix_menu.lower() == "1" or choix_menu.lower() == "lister les tâches":
            print("\n--- Voici la liste de vos tâches ---")
            if not taches:
                print("-> Aucune tâche pour le moment.")
            else:
                for t in taches:
                    date_creation = t.get('cree_le', 'N/A')
                    print(f"-> ID {t['id']}: {t['titre']} (Statut: {t['statut']}) - Créée le: {date_creation}")
            print("-" * 36 + "\n")

        elif choix_menu.lower() == "2" or choix_menu.lower() == "ajouter une tâche":
            titre_tache = input("Quel est le titre de la nouvelle tâche ? ")
            try:
                nouvelle_tache = creer_tache(taches, titre_tache)
                sauvegarder_taches(taches, FICHIER_TACHES)
                print(f"Tâche '{nouvelle_tache['titre']}' ajoutée avec succès !")
            except ValueError as e:
                print(f"Erreur : {e}")
            print("-" * 25 + "\n")

        # --- DÉBUT DE LA LOGIQUE DE MODIFICATION ---
        elif choix_menu.lower() == "3" or choix_menu.lower() == "modifier une tâche":
            try:
                id_a_modifier = int(input("Entrez l'ID de la tâche à modifier : "))
                tache_a_modifier = trouver_tache_par_id(taches, id_a_modifier)

                if tache_a_modifier:
                    nouveau_statut = input(f"Entrez le nouveau statut pour '{tache_a_modifier['titre']}' (actuel: {tache_a_modifier['statut']}) : ").strip()
                    if nouveau_statut: # S'assurer que l'utilisateur a bien entré quelque chose
                        tache_a_modifier['statut'] = nouveau_statut
                        tache_a_modifier['maj_le'] = date_tache() # On met à jour la date de modification
                        sauvegarder_taches(taches, FICHIER_TACHES)
                        print("Statut de la tâche mis à jour avec succès !")
                    else:
                        print("Le statut ne peut pas être vide. Modification annulée.")
                else:
                    print(f"Erreur : Aucune tâche trouvée avec l'ID {id_a_modifier}.")
            except ValueError:
                print("Erreur : L'ID doit être un nombre.")
            print("-" * 25 + "\n")
        # --- FIN DE LA LOGIQUE DE MODIFICATION ---

        # --- DÉBUT DE LA LOGIQUE DE SUPPRESSION ---
        elif choix_menu.lower() == "4" or choix_menu.lower() == "supprimer une tâche":
            try:
                id_a_supprimer = int(input("Entrez l'ID de la tâche à supprimer : "))
                tache_a_supprimer = trouver_tache_par_id(taches, id_a_supprimer)

                if tache_a_supprimer:
                    confirmation = input(f"Êtes-vous sûr de vouloir supprimer la tâche '{tache_a_supprimer['titre']}' ? (oui/non) ")
                    if confirmation.lower() == 'oui':
                        # On reconstruit la liste sans l'élément à supprimer
                        taches[:] = [t for t in taches if t['id'] != id_a_supprimer]
                        sauvegarder_taches(taches, FICHIER_TACHES)
                        print("Tâche supprimée avec succès !")
                    else:
                        print("Suppression annulée.")
                else:
                    print(f"Erreur : Aucune tâche trouvée avec l'ID {id_a_supprimer}.")
            except ValueError:
                print("Erreur : L'ID doit être un nombre.")
            print("-" * 25 + "\n")
        # --- FIN DE LA LOGIQUE DE SUPPRESSION ---

        else:
            print("Choix non valide, veuillez réessayer.")

except ValueError:
    print("Erreur inattendue.")