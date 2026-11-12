import random

def add_an_account(x):
    print("creation du compte en cours ...")
     comptes_bancaires  [compte()]= {
        "code" : code(),
        "solde" : solde(),
        "plafond" : 500
     }
    


def compte():
     numero_compte = str(random.randint(100000, 999999))
     while numero_compte in comptes_bancaires:
        numero_compte = str(random.randint(100000, 999999))
    return numero_compte

   





comptes_bancaires = {
    "123456": {"code": "4321", "solde": 1500, "plafond": 500},
    "654321": {"code": "0000", "solde": 45, "plafond": 200},
    "987654": {"code": "9999", "solde": 12000, "plafond": 1500}
}