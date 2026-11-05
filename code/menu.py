
from tools import*
from data import*


" quand le client entre son code de carte il est dirigé sur ce menu"



def consulter():
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    print(f"le solde de votre compte est de {solde}€")

def quitter():



nb = afficher_menu()

if nb == 1 :
    consulter()
elif nb == 2 :
    retrait()
elif nb == 3 :
    quitter()
else  :
    print ("le nombre saisi est incorrect")
  

