def debut():
    rep = input("Avez-vous déjà un compte ? (0 : non ; 1 : oui) : ")

    if rep == "0":
        print("Création d'un compte")

    elif rep == "1":
        print("Insertion de votre carte")

    else:
        print("Réponse incorrecte")


while True:
    debut()
    break