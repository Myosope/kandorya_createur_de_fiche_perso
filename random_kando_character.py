###ULTIMATE BRAVERY KANDORYA
import random
import copy

print("BIENVENUE SUR ULTIMATE BRAVERY KANDORYA")
#Ici les archetypes et competences sont traitees de la meme facon



class competence():
    def __init__(self, name_var,cost_var,prerequis_list):
        self.name= name_var
        self.cost= cost_var
        self.prerequis=prerequis_list
        self.spec="Null"
        self.description="Write description here"#TODO ajouter les descriptions
        self.types="Racial ou achat ou don ?" #TODO ajouter les descriptions

class sort(competence):
    def __init__(self, name_var,cost_var,prerequis_list):
        super().__init__(name_var,cost_var,prerequis_list)
        self.action = "Action par defaut"
        self.incantation = "Incatation par defaut"
        self.composant = "Composant par defaut"

class race():
    def __init__(self, name_var):
        self.name= name_var
        self.cost= 1
        self.spec="Null"
        self.description="Write description here"

class personnage():
    def __init__(self):
        self.xp=10
        self.name="Jean-Michel"
        self.competences=[]
        self.PV=2 #ne peut jamais depasser 5
        self.Pugilat_score=0
        self.race="Null"
        self.genre="Null"
        self.description="Write description here"



liste_genre = ["Homme","Femme","Autre"]
liste_immunite=["Coma","Sommeil",  "Silence",   "Douleur", "Nausee",    "Oubli",    "Langue morte","Lenteur",    "Petrification",  "Surdite",    "Verite"]
nb_competence_max=20 #par defaut

Liste_des_langages=["Commun","Targain","Shin","Mulq","Elfique","Orc","Nain","Abyssi"] #TODO

#############################CREATION DES COMPETENCES

liste_competences=[]#initialisation à vide


##############################Archetypes
artisan=    competence("Artisan",2,[[]])
liste_competences.append(artisan)

medecin=    competence("Medecin",4,[[]])
liste_competences.append(medecin)

magicien=     competence("Magicien",4,[[]])
liste_competences.append(magicien)

erudit=     competence("Erudit",2,[[]])
liste_competences.append(erudit)

roublard=   competence("Roublard",4,[[]])
liste_competences.append(roublard)

combattant= competence("Combattant",4,[[]])
liste_competences.append(combattant)


#=competence("",0,[])

##############################generiques
Assommer            =competence("Assommer",1,[[]])
liste_competences.append(Assommer)
Constitution_1      =competence("Constitution_1",3,[[]])
liste_competences.append(Constitution_1)
Constitution_2      =competence("Constitution_2",5,[[Constitution_1]])
liste_competences.append(Constitution_2)
Constitution_3      =competence("Constitution_3",7,[[Constitution_2]])
liste_competences.append(Constitution_3)
Crane_Epais         =competence("Crane_Epais",6,[[]])
liste_competences.append(Crane_Epais)
Explorateur         =competence("Explorateur",3,[[]])
liste_competences.append(Explorateur)
Immunite            =competence("Immunite",5,[[]])
Immunite.spec="Several"
liste_competences.append(Immunite)


Lire_Ecrire_Parler  =competence("Lire_Ecrire_Parler",1,[[]])
Lire_Ecrire_Parler.spec="Several"
liste_competences.append(Lire_Ecrire_Parler)

Mythes_et_Legendes  =competence("Mythes_et_Legendes",4,[[]])
liste_competences.append(Mythes_et_Legendes)
Noble               =competence("Noble",3,[[]])
liste_competences.append(Noble)
Pugilat             =competence("Pugilat",2,[[]])
Pugilat.spec="Infini"
liste_competences.append(Pugilat)
Richesses_1         =competence("Richesses_1",2,[[]])
liste_competences.append(Richesses_1)
Richesses_2         =competence("Richesses_2",4,[[Richesses_1]])
liste_competences.append(Richesses_2)
premier_secours     =competence("premier_secours",2,[[]])
liste_competences.append(premier_secours)
illetre             =competence("illetre",0,[[]])
liste_competences.append(illetre)

##############################artisan

Alchimiste                  =competence("Alchimiste",4,[[artisan]])
liste_competences.append(Alchimiste)
Apothicaire                 =competence("Apothicaire",4,[[artisan]])
liste_competences.append(Apothicaire)
Armurier                    =competence("Armurier",3,[[artisan]])
liste_competences.append(Armurier)
Bricoleur                   =competence("Bricoleur",3,[[artisan]])
liste_competences.append(Bricoleur)
Catalyste                   =competence("Catalyste",3,[[artisan]])
liste_competences.append(Catalyste)
Contrebandier               =competence("Contrebandier",2,[[artisan]])
liste_competences.append(Contrebandier)
Forgeron                    =competence("Forgeron",4,[[artisan,Armurier]])
liste_competences.append(Forgeron)
Grimoire_d_Apothicaire_1    =competence("Grimoire_d_Apothicaire_1",4,[[artisan,Apothicaire]])
liste_competences.append(Grimoire_d_Apothicaire_1)
Grimoire_d_Apothicaire_2    =competence("Grimoire_d_Apothicaire_2",4,[[artisan,Apothicaire,Grimoire_d_Apothicaire_1]])
liste_competences.append(Grimoire_d_Apothicaire_2)
Grimoire_d_Apothicaire_3    =competence("Grimoire_d_Apothicaire_3",4,[[artisan,Apothicaire,Grimoire_d_Apothicaire_2]])
liste_competences.append(Grimoire_d_Apothicaire_3)
Grimoire_d_Apothicaire_4    =competence("Grimoire_d_Apothicaire_4",4,[[artisan,Apothicaire,Grimoire_d_Apothicaire_3]])
liste_competences.append(Grimoire_d_Apothicaire_4)
Grimoire_d_Apothicaire_5   =competence("Grimoire_d_Apothicaire_5",4,[[artisan,Apothicaire,Grimoire_d_Apothicaire_4]])
liste_competences.append(Grimoire_d_Apothicaire_5)
Herboriste                  =competence("Herboriste",3,[[artisan]])
liste_competences.append(Herboriste)
Ingenieur                   =competence("Ingenieur",4,[[artisan,Bricoleur]])
liste_competences.append(Ingenieur)
Mineur                      =competence("Mineur",3,[[artisan]])
liste_competences.append(Mineur)
Mineur_Diamantaire          =competence("Mineur_Diamantaire",3,[[artisan]])
liste_competences.append(Mineur_Diamantaire)



##############################medecin
Diagnosticien               =competence("Diagnosticien",3,[[medecin]])
liste_competences.append(Diagnosticien)
Praticien                   =competence("Praticien",4,[[medecin,Diagnosticien]])
liste_competences.append(Praticien)
Barbier_Boucher             =competence("Barbier_Boucher",5,[[medecin,Praticien]])
liste_competences.append(Barbier_Boucher)

Homeopathe                  =competence("Homeopathe",0,[[medecin]])
liste_competences.append(Homeopathe)
Identifications_medical_1   =competence("Identifications_medical_1",3,[[medecin,]])
liste_competences.append(Identifications_medical_1)
Identifications_medical_2   =competence("Identifications_medical_2",4,[[medecin,Identifications_medical_1]])
liste_competences.append(Identifications_medical_2)

Soin_d_urgence              =competence("Soin_d_urgence",3,[[medecin]])
liste_competences.append(Soin_d_urgence)

##############################erudit
Identification_erudition_1  =competence("Identification_erudition_1",3,[[erudit]])
liste_competences.append(Identification_erudition_1)
Identification_erudition_2  =competence("Identification_erudition_2",4,[[erudit,Identification_erudition_1]])
liste_competences.append(Identification_erudition_2)
Ritualiste_1                =competence("Ritualiste_1",1,[[erudit]])
liste_competences.append(Ritualiste_1)
Ritualiste_2                =competence("Ritualiste_2",3,[[erudit,Ritualiste_1]])
liste_competences.append(Ritualiste_2)

##############################roublard

Assassinat                  =competence("Assassinat",16,[[roublard,Assommer]])
liste_competences.append(Assassinat)
Crochetage                  =competence("Crochetage",4,[[roublard]])
liste_competences.append(Crochetage)
Cambriolage                 =competence("Cambriolage",2,[[roublard]])
liste_competences.append(Cambriolage)
Contrebandier               =competence("Contrebandier",2,[[roublard,Crochetage]])
liste_competences.append(Contrebandier)
Deguisement                 =competence("Deguisement",3,[[roublard]])
liste_competences.append(Deguisement)
Vol                 =competence("Vol",0,[[roublard]])
liste_competences.append(Vol) # on retire vol descompetences disponibles car elle est automatiquement donnee par roublard


##############################magicien
Meditation                  =competence("Meditation",2,[[magicien]])
liste_competences.append(Meditation)
Familier_de_sort            =competence("Familier_de_sort",2,[[magicien]])
liste_competences.append(Familier_de_sort)
Livre_de_Sorts              =competence("Livre_de_Sorts",0,[[magicien]])
liste_competences.append(Livre_de_Sorts)

#combattant
Esquive                     =competence("Esquive",5,[[combattant]])
liste_competences.append(Esquive)
Intimidation                =competence("Intimidation",5,[[combattant]])
liste_competences.append(Intimidation)
Porte_banniere              =competence("Porte-banniere",3,[[combattant]])
liste_competences.append(Porte_banniere)
Porte_etendards             =competence("Porte-etendards",5,[[combattant,Porte_banniere]])
liste_competences.append(Porte_etendards)


##############################hybride
Ambidextre                  =competence("Ambidextre",2,[[roublard],[combattant]])
liste_competences.append(Ambidextre)
Contrebandier               =competence("Contrebandier",2,[[roublard],[artisan]])
liste_competences.append(Contrebandier)
Tatouages_magiques          =competence("Tatouages magiques",3,[[artisan],[erudit],[combattant]])
liste_competences.append(Tatouages_magiques)
Expert_aux_couteaux         =competence("Expert aux couteaux",2,[[roublard],[combattant]]) #Attention cette competence fait "planter" le programme..... planter... vous avez compris ? PLANTER !
liste_competences.append(Expert_aux_couteaux)
Instinct_de_survie          =competence("Instinct_de_survie",3,[[roublard],[combattant]])
liste_competences.append(Instinct_de_survie)



##############################RACE:
liste_race=[]
Humain                      =race("Humain")
liste_race.append(Humain)
Abyssi                      =race("Abyssi")
liste_race.append(Abyssi)
Aratois                     =race("Aratois")
liste_race.append(Aratois)
Elfe                        =race("Elfe")
liste_race.append(Elfe)
Faune                       =race("Faune")
liste_race.append(Faune)
Elfe_Noir                   =race("Elfe Noir")
liste_race.append(Elfe_Noir)
Lutin                       =race("Lutin")
liste_race.append(Lutin)
Nain                        =race("Nain")
liste_race.append(Nain)
Peau_verte                  =race("Peau verte")
liste_race.append(Peau_verte)
Troll                       =race("Troll")
liste_race.append(Troll)
Ogre                        =race("Ogre")
liste_race.append(Ogre)

###################################################Competences raciale

Eloquence = competence("Eloquence",0,[[]])

Malediction_de_l_eau= competence("Malediction de l'eau",0,[[]])

Agile= competence("",0,[[]])
Agile=copy.deepcopy(Esquive)
Agile.name="Agile"

Ame_sombre= competence("",0,[[]])
Ame_sombre=copy.deepcopy(Immunite)
Ame_sombre.name="Ame sombre"
Ame_sombre.spec="Verite"

Foyer_doux_foyer = competence("Foyer doux foyer",0,[[]])

Petit_mais_costaud= competence("Petit mais costaud",0,[[]])

Regeneration= competence("Regeneration",0,[[]])
Taper = competence("Taper",0,[[]])


###################################################
liste_sort=[]
###
Alarme                     =sort("Alarme",2,[[magicien]])
Alarme.action = "Au contact"
Alarme.incantation = "Incantation longue"
Alarme.composant = "Clochette + ficelle"

liste_sort.append(Alarme)
###
Analyse_de_psyche          =sort("Analyse_de_psyche",3,[[magicien]])
liste_sort.append(Analyse_de_psyche)
###
Armure_Magique             =sort("Armure_Magique",3,[[magicien]])
liste_sort.append(Armure_Magique)
###
Barriere_magique           =sort("Barriere_magique",3,[[magicien]])
liste_sort.append(Barriere_magique)
###
Capture_d_ame              =sort("Capture_d_ame",5,[[magicien]])
liste_sort.append(Capture_d_ame)
###
Champ_d_energie            =sort("Champ_d_energie",3,[[magicien]])
liste_sort.append(Champ_d_energie)
###
Desarmement                =sort("Desarmement",3,[[magicien]])
liste_sort.append(Desarmement)
###
Detection_magique          =sort("Detection_magique",3,[[magicien]])
liste_sort.append(Detection_magique)
###
Dissipation_de_barriere    =sort("Dissipation_de_barriere",3,[[magicien]])
liste_sort.append(Dissipation_de_barriere)
###
Duplication_de_souvenir    =sort("Duplication_de_souvenir",6,[[magicien]])
liste_sort.append(Duplication_de_souvenir)
###
Entraves                   =sort("Entraves",4,[[magicien]])
liste_sort.append(Entraves)
###
Faire_Parler_un_Mort       =sort("Faire_Parler_un_Mort",5,[[magicien]])
liste_sort.append(Faire_Parler_un_Mort)
###
Flammeche=sort("Flammeche",1,[[magicien]])
liste_sort.append(Flammeche)
###
Langue_morte               =sort("Langue_morte",2,[[magicien]])
liste_sort.append(Langue_morte)
###
Lenteur                    =sort("Lenteur",4,[[magicien]])
liste_sort.append(Lenteur)
###
Localisation               =sort("Localisation",6,[[magicien]])
liste_sort.append(Localisation)
###
Lumiere                    =sort("Lumiere",1,[[magicien]])
liste_sort.append(Lumiere)
###
Nausee                     =sort("Nausee",2,[[magicien]])
liste_sort.append(Nausee)
###
Peur                       =sort("Peur",5,[[magicien]])
liste_sort.append(Peur)
###
Projectile_magique_1       =sort("Projectile_magique_1",2,[[magicien]])
liste_sort.append(Projectile_magique_1)
###
Projectile_magique_2       =sort("Projectile_magique_2",4,[[magicien,Projectile_magique_1]])
liste_sort.append(Projectile_magique_2)
###
Projectile_magique_3       =sort("Projectile_magique_3",6,[[magicien,Projectile_magique_2]])
liste_sort.append(Projectile_magique_3)
###
Rafale_de_vent             =sort("Rafale_de_vent",3,[[magicien]])
liste_sort.append(Rafale_de_vent)
###
Soin_necromantique         =sort("Soin_necromantique",3,[[magicien]])
liste_sort.append(Soin_necromantique)
###
Sommeil                    =sort("Sommeil",3,[[magicien]])
liste_sort.append(Sommeil)
###
Silence                    =sort("Silence",4,[[magicien]])
liste_sort.append(Silence)
###
Surdite                    =sort("Surdite",3,[[magicien]])
liste_sort.append(Surdite)
###
Transfert_de_vie           =sort("Transfert_de_vie",6,[[magicien]])
liste_sort.append(Transfert_de_vie)
###
Verite                     =sort("Verite",6,[[magicien]])
liste_sort.append(Verite)
###
liste_competences.extend(liste_sort)
###################################################

#TODO : Liste des crafts

###################################################



Mon_personnage = personnage()
Mon_personnage.xp=int(input("Nombre d'XP ? \n"))
nb_competence_max=int(input("Nombre de competences maximales ?\n"))


def ajout_genre(perso, choix):
    if choix == True:
    	genre_choisi = False
    	while genre_choisi not in liste_genre:
    		genre_choisi = str(input("Veuillez choisir un genre parmi la liste suivante : " + str(liste_genre) +"\n"))
    		if genre_choisi not in liste_genre:
    			print("Erreur: veuillez entrer un des genre proposes (respectez la case).")
    else:
    	genre_choisi = random.choice(["Homme","Femme"])
    perso.genre=genre_choisi
    if(genre_choisi =="Homme"):
        perso.name="Jean-Michel"
    elif(genre_choisi =="Femme"):
        perso.name="Jeanne-Micheline"
    else:
        perso.name="Null"


def ajout_race(perso,choix):
    if choix == True:
    	nom_race_choisie = False
    	liste_nom_race =[]
    	for race in liste_race:
    			liste_nom_race.append(race.name )
    	while nom_race_choisie not in liste_nom_race:
    		
    		
    		nom_race_choisie = str(input("Veuillez choisir une race parmi la liste suivante : " + str(liste_nom_race)+"\n" ))
    		if nom_race_choisie not in liste_nom_race:
    			print("Erreur: veuillez entrer une des race proposees (respectez la case).")
    	for race in liste_race:
    		if race.name == nom_race_choisie:
    			race_choisie = race
    		else:
    			None
    		
    else:
    	race_choisie = random.choice(liste_race)



    langue_raciale=competence("new",0,[])
    langue_raciale=copy.deepcopy(Lire_Ecrire_Parler)
    langue_raciale.spec=str(race_choisie.name)



    if race_choisie.name==Abyssi.name :
        perso.competences.append(langue_raciale)
        perso.competences.append(Mythes_et_Legendes)
        if perso.genre == "Homme":
            perso.competences.append(Eloquence)
        elif perso.genre == "Femme":
            perso.competences.append(Malediction_de_l_eau)
        else:
            None

    elif race_choisie.name== Aratois.name  :
        perso.competences.append(langue_raciale)
        perso.competences.append(artisan)
        Immunite_maladie_non_magique =copy.deepcopy(Immunite)
        Immunite_maladie_non_magique.spec="Maladie non-magique"
        perso.competences.append(Immunite_maladie_non_magique)

    elif race_choisie.name==Elfe.name :
        perso.competences.append(langue_raciale)
        perso.PV=perso.PV+1

    elif race_choisie.name== Faune.name:
        perso.competences.append(langue_raciale)
        perso.competences.append(Agile)
        Herboriste.cost=1

    elif race_choisie.name==Elfe_Noir.name :
        perso.competences.append(langue_raciale)
        perso.competences.append(Ame_sombre)

    elif race_choisie.name== Lutin.name:
        perso.competences.append(langue_raciale)
        roublard.cost=2
        perso.competences.append(Foyer_doux_foyer)

    elif race_choisie.name== Nain.name:
        perso.competences.append(langue_raciale)
        perso.competences.append(Petit_mais_costaud)

    elif race_choisie.name== Peau_verte.name :
        perso.competences.append(langue_raciale)
        perso.competences.append(Regeneration)

    elif race_choisie.name== Troll.name :
        print("C'est un troll !")
        perso.competences.append(langue_raciale)
        perso.competences.append(Regeneration)

    elif race_choisie.name== Ogre.name :
        perso.competences.append(langue_raciale)
        perso.competences.append(Taper)
        perso.Pugilat_score = perso.Pugilat_score+2

    else:
        None

    langue_commune=competence("new",0,[])
    langue_commune = copy.deepcopy(Lire_Ecrire_Parler)
    langue_commune.spec=str("Commun")

    perso.competences.append(langue_commune)
    perso.race=race_choisie


def ajout_competences(perso,choix):
    #Creation personnage


    #Mise a jour des competences disponibles:
    #on parcourt les competences existantes et si les pre requis sont remplis
    #Elles ne doivent pas etre deja acquises
    #Et on doit avoir les pre-requis
    #Et peut se payer le cout

    liste_competences
    check = False

    for i in range(1,nb_competence_max):
        liste_competences_dispo=[]
        #print ("Tour : " + str(i) )
        for element in liste_competences:
            #print ("Nom de la competence revue : " + str(element.name))
            #print ("XP disponible : " + str(perso.xp))
            if element.cost <=perso.xp:
                #print("La competence est achetable")


                owned=False
                for my_competence in perso.competences:
                    if element.name == my_competence.name:
                        #print("La competence est deja prise")
                        if element.spec == my_competence.spec and element.spec != "Infini":
                            owned=True

                    else:
                        None

                if owned ==False:
                    #traitement sur les prerequis:
                    if element.prerequis==[]:
                        #print("La competence n'a pas de pre-requis")
                        liste_competences_dispo.append(element)
                    else:

                        for ensemble_prerequis in element.prerequis:
                            check=False
                            #print(ensemble_prerequis)
                            #print(perso.competences)

                            #check =  all(item in perso.competences for item in ensemble_prerequis)
                            counter =0
                            for elem_prerequis in ensemble_prerequis:
                                for elem_perso in perso.competences:
                                    if elem_perso.name == elem_prerequis.name:
                                        counter = counter +1
                            if counter ==len(ensemble_prerequis):
                                check = True

                            if check:
                                break #on a trouve un sous ensemble qui correspond a ce que l'on veux.
                            else:
                                None #on continue de voir les sous ensembles de pre-requis
                        if check:
                            #print("ajout de element")
                            liste_competences_dispo.append(element)
                        else:
                            None
                            #print("La competence: " +element.name +" n'est pas disponible.")
                else:
                    #print("La competence " +element.name +" est deja prise")
                    None

            else:
                None
                #print("La competence "+element.name + "est trop chere")



        #print("Display de la liste des elements dispo")
        liste_competences_dispo_name=[]
        for element in liste_competences_dispo:
            liste_competences_dispo_name.append(element.name)
        #print(liste_competences_dispo_name)

        if (liste_competences_dispo==[]):
            #print("Plus de competence disponibles")
            break
        else:
            #AJOUT DES COMPETENCES
            if choix == True:
                nom_competence_choisie = False
                liste_nom_competence =[]  
                liste_nom_competence_pure =[]
                liste_nom_sort =[]                                
                for comp in liste_competences_dispo:
                    liste_nom_competence.append(comp.name )
                    if  (type(comp) is sort):
                        liste_nom_sort.append(comp.name)
                    else:
                        liste_nom_competence_pure.append(comp.name)

                while nom_competence_choisie not in liste_nom_competence:
                    if (liste_nom_sort==[]):
                        nom_competence_choisie = str(input("Veuillez choisir une competence parmi la liste suivante : \n" + str(liste_nom_competence_pure)+"\n"))
                    else:    
                        nom_competence_choisie = str(input("Veuillez choisir une competence parmi la liste suivante : \n" + str(liste_nom_competence_pure) +"\nOu bien un sort de la liste suivante : \n" + str(liste_nom_sort) +"\n"))
                   
                    
                    if nom_competence_choisie not in liste_nom_competence:
                        print("Erreur: veuillez entrer une des competence proposees (respectez la case).")
        		
                print( "nom_competence_choisie : " + str(nom_competence_choisie))
                for comp in liste_competences_dispo:
                    if comp.name == nom_competence_choisie:
                        competence_choisie = comp
                    else:
                        None
            else:
                competence_choisie = random.choice(liste_competences_dispo)

            #traitement speciaux
            #print("competence_choisie : " + competence_choisie.name)
            if competence_choisie.name == erudit.name:
                for i in range (0,2): # on ajoute deux Lire_Ecrire_Parler
                    new_competence=competence("new",0,[])
                    new_competence = copy.deepcopy(Lire_Ecrire_Parler)		
                    if new_competence.spec=="Several":
                        new_competence.spec =  str(input("Entrez une langue pour " + str(new_competence.name) + " parmi les suivantes : \n" + str(Liste_des_langages) + " \n"))
                        spec_deja_acquise = False
                        while spec_deja_acquise == False:
                            #if Mon_personnage.competences !=[]:
                            for comp in Mon_personnage.competences:
                                if str(comp.spec) == str(new_competence.spec) and comp.spec!="Null":
                                    #cette specificite de competence a deja ete choisie
                                    new_competence.spec=str(input("Cette specialite a deja ete choisie.\nVeuillez en choisir une autre specialite de la competence du type " + new_competence.name +" : \n"))
                                    spec_deja_acquise = False
                                    break 
                                spec_deja_acquise = True
                            #la specialite n'a jamais encore ete acquise.
                    perso.competences.append(new_competence)
                    
                #changement du cout de Mythe et legende
                Mythes_et_Legendes.cost=2

            elif competence_choisie.name==roublard.name:
                perso.competences.append(Vol)
                #print("Ajout de Vol grace a roublard")
            elif competence_choisie.name==magicien.name:
                perso.competences.append(Livre_de_Sorts)
                #print("Ajout de Livre_de_Sorts grace a mage")
            elif competence_choisie.name==medecin.name:
                perso.competences.append(premier_secours)
                #print("Ajout de 1er secours")
            elif competence_choisie.name==combattant.name or competence_choisie.name==Constitution_1.name or competence_choisie.name==Constitution_2.name or competence_choisie.name==Constitution_3.name:
                perso.PV=perso.PV+1
                #print("Ajout de PV")

            elif competence_choisie.name==Apothicaire.name:
                perso.competences.append(Grimoire_d_Apothicaire_1)
                #print("Ajout de 1er secours")

            elif competence_choisie.name==Pugilat.name:
                perso.Pugilat_score=perso.Pugilat_score+1
                #print("Ajout de Pujilat")
            else:
                None
                #print("Pas de cas specifique")
            new_competence=competence("new",0,[])
            new_competence = copy.deepcopy(competence_choisie)
            
            if new_competence.spec=="Several":
                if new_competence.name == "Immunite":
                        print(str(liste_immunite))
        
                new_competence.spec =  str(input("Specialite de la competence pour " + str(new_competence.name) + "?\n"))
        
                spec_deja_acquise = False
                while spec_deja_acquise == False:
                    #if Mon_personnage.competences !=[]:
                    for comp in Mon_personnage.competences:
                        if str(comp.spec) == str(new_competence.spec) and comp.spec!="Null":
                            #cette specificite de competence a deja ete choisie
                            new_competence.spec=str(input("Cette specialite a deja ete choisie.\n Veuillez en choisir une autre competence du type " + competence_choisie.name +" : \n"))
                            spec_deja_acquise = False
                            break 
                        spec_deja_acquise = True
                    #la specialite n'a jamais encore ete acquise.
        
    
                 




            owned=False
            if new_competence.name==Pugilat.name:
                for my_competence in perso.competences:
                        if new_competence.name == my_competence.name:
                            #print("La competence est deja prise")
                            owned=True
                            break
                        else:
                            None

            if owned:
                perso.xp=perso.xp-new_competence.cost
            else:
                #print("Ajout de la competence : " +new_competence.name)
                perso.competences.append(new_competence)
                perso.xp=perso.xp-new_competence.cost


            #print("Etat" + str(i))
            #affiche_personnage(perso)
        affiche_personnage(Mon_personnage)
        print("\n--------\n")
        if (perso.xp==0):
            #print("Plus d'xp a depenser")
            break


def affiche_personnage(perso):
    print("Nom: " +perso.name)
    print("Genre: " + str(perso.genre))
    print("Race: " + str(perso.race.name))
    print("XP: " + str(perso.xp))
    print("PV: " + str(perso.PV))
    print("Pugilat: " + str(perso.Pugilat_score))
    competence_liste=[]
    for element in perso.competences:
        if element.spec != "Null" and element.spec != "Infini":
            competence_liste.append(element.name + " (" + element.spec+")" )
        else:
            competence_liste.append(element.name)

    print("Competences: " + str(competence_liste))

def verification(perso):
    competence_liste=[]
    for element in perso.competences:
       competence_liste.append(element.name)
    verif = len(competence_liste) != len(set(competence_liste))
    return verif


#### CHOIX D'UNE GENERATION ALEATOIRE OU NON
Mon_choix = str(input("Voulez vous faire votre personnage vous-meme ? (OUI ou NON)\n"))
if Mon_choix == "OUI":
    Mon_choix = True
else:
    Mon_choix =False


ajout_genre(Mon_personnage,Mon_choix)
print("Genre:" + str(Mon_personnage.genre))

ajout_race(Mon_personnage,Mon_choix)
print("Genre:" + str(Mon_personnage.race.name))

ajout_competences(Mon_personnage,Mon_choix)
print("ETAT FINAL")
affiche_personnage(Mon_personnage)



#Verification qu'il n'y a pas de competence en double:
print("Verif :" +str(verification(Mon_personnage) ))
print ("FIN")

