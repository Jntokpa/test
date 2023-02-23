#le menu

<<<<<<< HEAD
    rep = input("1 : Ajouter \n 2 : Afficher la liste \n")
    rep = int(rep)
#modif by Hari
#modif by JN
=======
rep = input("1 : Ajouter \n 2 : Afficher la liste \n")
rep = int(rep)
print("nenin"#nenin)
>>>>>>> fofana
if rep == 1:
    nom = input("donner votre nom \n")
    prenoms = input("donner vos prenom \n")
    mail = input("donner votre mail \n")
    numero = input("donner votre numero \n")
    import datetime
    date_saisir = datetime.datetime.now()
    jour =(date_saisir.strftime("%d"))
    mois = (date_saisir.strftime("%m"))
    annee = (date_saisir.strftime("%Y"))
    date_saisir = jour+" "+mois+" "+annee

    tab = [date_saisir," ", nom," ", prenoms," ", mail," ", numero]
    filout = open("zoo1.txt", "a")
    for x in tab :
        filout.write(x)

    filout.write("\n")
    filout.close()
#
elif rep == 2 :
    chaine = input("donner svp la date de saisir sous le format suivant jj mm aaaa  \n")
    filout = open("zoo1.txt", "r")
    for x in filout :
        if chaine in x :
            print(x)
    filout.close()

