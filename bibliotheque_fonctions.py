import json

fichier = "bibliotheque.json"

# Vérifier si le fichier existe
def fichier_existe():
    f = open(fichier, "r")
    f.close()
    return True

# Charger les livres
def charger_livres():
    livres = []
    if fichier_existe():
        f = open(fichier, "r")
        livres = json.load(f)
        f.close()
    return livres

#sauvgarde :
def sauvegarder_livres(livres):
    f = open(fichier, "w")
    json.dump(livres, f)
    f.close()

# Ajouter un nouveau livre
def ajouter_livre(livres):
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    annee = input("Année de publication : ")

    if annee.isdigit():
        annee = int(annee)
    else:
        print("Erreur : l'année doit être un nombre")
        return

    if len(livres) == 0:
        nouvel_id = 1
    else:
        dernier_id = livres[-1]["ID"]
        nouvel_id = dernier_id + 1

    livre = {
        "ID": nouvel_id,
        "Titre": titre,
        "Auteur": auteur,
        "Année": annee,
        "Lu": False,
        "Note": None
    }

    livres.append(livre)
    print("Livre ajouté avec succès.")

#Supprimer un livre par ID
def supprimer_livre(livres):
    id_str = input("Entrez l'ID du livre à supprimer : ")
    if id_str.isdigit():
        id_livre = int(id_str)
        trouve = False
        for livre in livres:
            if livre["ID"] == id_livre:
                print("Voulez-vous vraiment supprimer :", livre["Titre"], "de", livre["Auteur"],  "?")
                confirmation = input("Tapez oui pour confirmer : ")
                if confirmation == "oui":
                    livres.remove(livre)
                    print("Livre supprimé.")
                else:
                    print("Suppression annulée.")
                trouve = True
                break
        if not trouve:
            print("Aucun livre avec cet ID.")
    else:
        print("ID invalide.")

#Rechercher un livre par mot-clé
def rechercher_livre(livres):
    mot_cle = input("Mot-clé à rechercher : ")
    resultats = []
    for livre in livres:
        if mot_cle in livre["Titre"] or mot_cle in livre["Auteur"]:
            resultats.append(livre)

    if len(resultats) == 0:
        print("Aucun livre trouvé")
    else:
        for livre in resultats:
            print("ID :", livre["ID"])
            print("Titre :", livre["Titre"])
            print("Auteur :", livre["Auteur"])
            print("Année :", livre["Année"])
            print("Lu :", livre["Lu"])
            print("Note :", livre["Note"])
            print("-----------------------")

#Marquer un livre comme lu + attribuer une note et commentaire
def marquer_comme_lu(livres):
    id_str = input("Entrez l'ID du livre lu : ")
    if id_str:
        id_livre = int(id_str)
        for livre in livres:
            if livre["ID"] == id_livre:
                livre["Lu"] = True
                note_str = input("Note sur 10 : ")
                if note_str:
                    livre["Note"] = int(note_str)
                else:
                    livre["Note"] = None
                commentaire = input("Commentaire: ")
                livre["Commentaire"] = commentaire
                print("Livre mis à jour.")
                return
        print("Aucun livre trouvé avec cet ID.")
    else:
        print("ID invalide.")

#Afficher les livres lus ou non lus
def filtrer_livres(livres):
    choix = input("Tapez 1 pour les livres lus, 2 pour les non lus : ")
    if choix == "1":
        etat = True
    elif choix == "2":
        etat = False
    else:
        print("Choix invalide.")
        return

    trouve = False
    for livre in livres:
        if livre["Lu"] == etat:
            print("ID :", livre["ID"])
            print("Titre :", livre["Titre"])
            print("Auteur :", livre["Auteur"])
            print("Année :", livre["Année"])
            print("Lu :", livre["Lu"])
            print("Note :", livre["Note"])
            print("-----------------------")
            trouve = True
    if not trouve:
        print("Aucun livre dans cette catégorie.")

#Trier les livres (année, auteur, note)
def trier_livres(livres):
    print("Trier par :")
    print("1. Année")
    print("2. Auteur")
    print("3. Note")
    choix = input("Votre choix : ")

    if choix == "1":
        livres.sort(key=lambda livre: livre["Année"])
    elif choix == "2":
        livres.sort(key=lambda livre: livre["Auteur"].lower())
    elif choix == "3":
        livres.sort(key=lambda livre: (livre["Note"] is None, livre["Note"]))
    else:
        print("Choix invalide.")
        return

    print("Livres triés :")
    afficher_livres(livres)

# Afficher tous les livres
def afficher_livres(livres):
    if len(livres) == 0:
        print("Aucun livre trouvé.")
    else:
        for livre in livres:
            print("ID :", livre["ID"])
            print("Titre :", livre["Titre"])
            print("Auteur :", livre["Auteur"])
            print("Année :", livre["Année"])
            print("Lu :", livre["Lu"])
            print("Note :", livre["Note"])
            print("-----------------------")