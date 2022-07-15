
def tri_personnalise(e):
    return len(e)

def afficher(collection):
    print(f"--------------LISTE DES PIZZAS ({len(collection)})-----------")
    # collection.sort(reverse=True)  Permet de trier dans le sens inverse
    collection.sort(key=tri_personnalise)   # Tri personnalisé
    if len(collection) == 0:
        print("AUCUNE PIZZA")
    else:
        for i in collection:
            print(i)
        print()
        print(f"Premiere pizza: {collection[0]}")
        print(f"Derinere pizza: {collection[-1]}")

def ajouter_pizza_utilisateur(collection):
    pizza_ajoute = input("Ajoutez une pizza: ")
    # p_existe = pizza_existe(pizza_ajoute,collection)
    if pizza_ajoute.lower() in collection:
        print("La pizza existe déjà")
    else:
        collection.append(pizza_ajoute)
        print("")
        print("Pizza Ajouté")

def pizza_existe(pizza, liste_pizza):
    for i in liste_pizza:
        if pizza == i:
            return True
    return False


pizzas =["4 Fromage", "végétarienne", "hawaienne", "calzone","orientale"]

vide =()
ajouter_pizza_utilisateur(pizzas)
afficher(pizzas)