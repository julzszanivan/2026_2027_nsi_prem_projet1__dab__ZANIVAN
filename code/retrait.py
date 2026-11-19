def retrait():
    print ("===========")
    print ("--Retrait--")
    print ("===========")
    plafond = 300
    solde = 500
    i = 0
    while i==0:
        try:
            montant_donne = float(input("Veuillez entrer un montant à retirer:"))
            if montant_donne%10 != 0:
                print ("Veuillez entrer une valeur divisible par 10.")
            elif montant_donne>plafond:
                print ("Vous avez dépassé votre plafond, veuillez remettre une valeur inférieur à celui-ci.")
            elif montant_donne>solde:
                print ("Vous n'avez pas assez d'argent pour retirer cette somme, veuillez remettre une valeur inférieur a votre solde.")
            elif montant_donne<=0:
                print ("Veuillez entrer une valeur supérieur à 0")
            else:
                print ("Action réussie, cette somme a été débité de votre compte.")
                print (f"Votre solde est maintenant de: {solde-montant_donne}€")
                i=1
    
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")
                          
retrait()
        