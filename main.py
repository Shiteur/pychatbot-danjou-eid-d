from fonctions import *
# appelle la fonction list_of_files
directory = "speeches"
files_names = list_of_files(directory, "txt")
# appelle la fonction convertion_minuscule
convertion_minuscule()
surpession_ponctuation()

def menu():
    print("Menu:")
    print("1. Afficher la liste des mots les moins importants")
    print("2. Afficher le mot avec le score TD-IDF le plus élevé")
    print("3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac")
    print("4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation »")
    print("5. Indiquer le premier président à parler du climat et/ou de l'écologie")
    print("6. Mot(s) évoqués par tous les présidents (hormis les mots non importants)")

while True:
    menu()
    choix = input("Choisissez une option: ")
    if choix == "1":
        mots_non_importants = mot_pas_important()
        print("Mots non importants:", mots_non_importants)
    elif choix == "2":
        mot_tfidf_max = mot_important()
        print("Mot(s) avec le score TD-IDF le plus élevé:", mot_tfidf_max)
    elif choix == "3":
        mots_chirac = mot_plus_repeter_par_chirac()
        print("Mot(s) le(s) plus répété(s) par le président Chirac:", mots_chirac)
    elif choix == "4":
        nation()
    elif choix == "5":
        ecologie()
    elif choix == "6":
        mots_evoques()
    else:
        print("Choix invalide.")


