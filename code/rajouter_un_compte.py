import random

def add_an_account():
    print("creation du compte en cours ...")
    comptes_bancaires  [numero]= {
        "code" : cod,
        "solde" : sold,
        "plafond" : plafond
     }
    print (f"-----votre compte a été créé : ID : {numero}----- ")
    print (f"-----code PIN : {cod}-----")
    print (f"-----solde: {sold} € -----")
    print (f"-----plafond : {plafond} € -----")


def compte():
    numero_compte = str(random.randint(100000, 999999))
    while numero_compte in comptes_bancaires:
        numero_compte = str(random.randint(100000, 999999))
    return numero_compte


def code():
    code = str(random.randint(1000, 9999))
    return code 

def solde():
    solde = int(input("Combien d'argent voulez-vous placer sur votre compte ? (entre 100 et 9 999 €) : "))

    while solde < 100 or solde > 9999:
        solde = int(input("Montant invalide. Entrez un montant entre 100 et 9 999 € : "))

    return solde


   
comptes_bancaires = {
    "123456": {"code": "4321", "solde": 1500, "plafond": 500},
    "654321": {"code": "0000", "solde": 45, "plafond": 200},
    "987654": {"code": "9999", "solde": 12000, "plafond": 1500}
}
numero = compte()
cod = code()
sold = solde()
plafond =  500 

add_an_account()


