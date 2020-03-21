# bot.py
def LoupGarou (N):
    import random as rd
    """
    Permet de jouer au Loup Garou avec N personnes (N>=8)
    L : liste avec les noms, les rôles, les caractéristiques du perso (nombre de pouvoir restant, statut de maire/ en couple
    Noms : liste avec seulement les noms


    Organisation de L pour une personne : "Noms", #chiffre correspondant au rôle, #chiffre de statut (maire, en couple, etc ...), #chiffre/ liste de chiffres de pouvoir restant pour 1 partie, #Chiffre état de vie (0 == mort, 1 == vivant)

    #Chiffre des rôles :
    Villageois : 0
    Loup : 1
    Sorcière : 2
    Voyante : 3
    Chasseur : 4
    Cupidon : 5

    """

    #Initialisation globale

    if type(N)!=int or N<8:
        return "Il faut placer en entrée un entier, et le nombre de jouers minimum est de 8"
    L,Noms=[0]*5*N,[0]*N    #Initialisation
    for i in range(len(Noms)):
        while Noms[i]==0 or Noms[i]=="":
            print("")
            print("Joueur",i+1)
            print("")
            Noms[i]=input("Rentrer le nom du joueur : ")
    for i in range(N):
        L[5*i]=Noms[i]  #On insère dans la liste finale le nom de tous les joueurs
        L[5*i+4]=1

    #Génération et attribution des rôles :

    if N<12:    #On calcule le nombre de loups garous
        NbL=2
    else:
        NbL=N//6
    Lo,S,Vo,Cha,Cu,n=1,2,3,4,5,0     #On attribue à chaque rôle un chiffre pour le répérer. On pose par principe Villageois == 0

    #On génère des nombres aléatoires, afin d'attribuer aléatoirement à NbL joueurs le rôle de Loup Garou. #Chiffre Loup Garou : 1

    while (NbL-n)!=0:
        i=rd.randint(0,N-n)
        if L[5*i+1]==0:
            L[5*i+1]=Lo
            n+=1

    #Attribution rôle sorcière. #Chiffre rôle Sorcière : 2

    i=rd.randint(0,N-NbL)
    if L[5*i+1]==0:
        L[5*i+1],L[5*i+3]=S,[1,1]  #Le [1,1] correspond aux pouvoirs de la sorcière : le 1er chiffre correspond au nombre de potions de vie restantes, le 2ème au nombre de potions de mort restantes
    else:   #Si le joueur i a déjà un rôle, alors on prend le suivant qui n'en a pas
        n=1
        while n==1:
            i+=1
            i=i%N
            if L[5*i+1]==0:
                L[5*i+1],L[5*i+3]=S,[1,1] #Le [1,1] correspond aux pouvoirs de la sorcière : le 1er chiffre correspond au nombre de potions de vie restantes, le 2ème au nombre de potions de mort restantes
                n=0

    #Attribution rôle Voyante. #Chiffre Voyante : 3

    i=rd.randint(0,N-NbL-1)
    if L[5*i+1]==0:
        L[5*i+1]=Vo
    else:   #Si le joueur i a déjà un rôle, alors on prend le suivant qui n'en a pas
        n=1
        while n==1:
            i+=1
            i=i%N
            if L[5*i+1]==0:
                L[5*i+1]=Vo
                n=0

    #Attribution rôle Chasseur. #Chiffre Chasseur : 4

    i=rd.randint(0,N-NbL-2)
    if L[5*i+1]==0:
        L[5*i+1]=Cha
    else:   #Si le joueur i a déjà un rôle, alors on prend le suivant qui n'en a pas
        n=1
        while n==1:
            i+=1
            i=i%N
            if L[5*i+1]==0:
                L[5*i+1]=Cha
                n=0

    #Attribution rôle Cupidon. #Chiffre Cupidon : 5

    i=rd.randint(0,N-NbL-3)
    if L[5*i+1]==0:
        L[5*i+1]=Cu
    else:   #Si le joueur i a déjà un rôle, alors on prend le suivant qui n'en a pas
        n=1
        while n==1:
            i+=1
            i=i%N
            if L[5*i+1]==0:
                L[5*i+1]=Cu
                n=0

    #Génération liste rôle/ Loup
    Role = ["Villageois","Loup Garou","Sorcière", "Voyante", "Chasseur", "Cupidon"]
    Loup=[]
    for i in range(N):
        if L[5*i+1]==1:
           Loup.append(i)

    #Lancement de la partie

    Jour=1

    print("Bienvenue dans le jeu du Loup Garou ! Vous êtes un village de",N,"habitants. Depuis fin 2019, la pandémie du Covid-19 se propage de plus en plus dans votre village, transformant les habitants de votre paisible village en Loups Garous, monstres assoifés de sang. Un compte rendu du village a initié la chasse aux Loups Garous.")
    print("Il y a donc 2 camps :")
    print("")
    print("- Le camp du village, avec les villageois, la sorcière, la voyante, le chasseur et Cupidon")
    print("")
    print("- Le camp des Loups Garous, composé des Loups")
    print("")
    print("Règles du jeu :")
    print("")
    print("Chaque camp doit éradiquer le plus vite possible le camp adverse")
    print("")
    print("Il y a",N,"joueurs. Voici la répartition :")
    print("")
    print("-",N-NbL-4,"villageois")
    print("-",NbL,'\x1b[6;31;40m' + "Loups Garous" + '\x1b[0m')
    print('\x1b[7;35;40m' + "- 1 sorcière" + '\x1b[0m')
    print('\x1b[7;33;40m' + "- 1 voyante" + '\x1b[0m')
    print('\x1b[7;36;40m' + "- 1 chasseur" + '\x1b[0m')
    print('\x1b[7;32;40m' + "- 1 sorcière" + '\x1b[0m')

