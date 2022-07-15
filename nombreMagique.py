# -------------------------------------------------------------------------------------------------------------------
import random


def demander_nombre(nb_min, nb_max):
    # Quel est le nombre magique (entre 1 et 10)
    # Return int

    nb_magique_int = 0
    while nb_magique_int == 0:
        nb_magique_str = input("Entrer un nombre magique entre " + str(nb_min) + " et " + str(nb_max) + " : ")
        try:
            nb_magique_int = int(nb_magique_str)
        except:
            print("ERREUR : Vous devez rentrer un nombre. Réessayez.")
        else:
            if nb_magique_int < nb_min or nb_magique_int > nb_max:
                print(f"ERREUR: Le nombre doit être entre {nb_min} et {nb_max}. Réessayer.")
                nb_magique_int = 0

    return nb_magique_int


# -------------------------------------------------------------------------------------------------------------------

# Initialisation de constante

NOMBRE_MIN = 1

NOMBRE_MAX = 10

NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)

NB_VIES = 4

# -------------------------------------------------------------------------------------------------------------------
# AFFICHAGE
# le nombre magique est plus petit
# le nombre magique est plus grand
# bravo vous avez gagné

nombre = 0

vies = NB_VIES

while not nombre == NOMBRE_MAGIQUE and vies > 0 :
    print("")
    print(f"Il vous reste {vies} chance.")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies -= 1
    else:
        print("Le nombre magique est plus grand")
        vies -= 1
if vies == 0:
    print("Vous avez perdu!")
    print(f"Le nombre magique était {NOMBRE_MAGIQUE}. Dommage.")
