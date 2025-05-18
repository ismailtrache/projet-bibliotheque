from bibliotheque_fonctions import *

#Menu
def menu():
    livres = charger_livres()

    while True:
        print("\n=== MENU DE LA BIBLIOTEQUE DE ISMAIL TRACHE ==")
        print("1. Afficher tous les livres")
        print("2. Ajouter un livre")
        print("3. Supprimer un livre")
        print("4. Rechercher un livre")
        print("5. Marquer un livre comme lu")
        print("6. Afficher livres lus / non lus")
        print("7. Trier les livres")
        print("8. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            afficher_livres(livres)
        elif choix == "2":
            ajouter_livre(livres)
        elif choix == "3":
            supprimer_livre(livres)
        elif choix == "4":
            rechercher_livre(livres)
        elif choix == "5":
            marquer_comme_lu(livres)
        elif choix == "6":
            filtrer_livres(livres)
        elif choix == "7":
            trier_livres(livres)
        elif choix == "8":
            sauvegarder_livres(livres)
            print("Sauvegarde effectuée. À bientôt.")
            break
        else:
            print("Choix invalide.")

menu()
