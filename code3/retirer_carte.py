from code3.menu_programme import*


# ==========================================
# RETIRER LA CARTE
# ==========================================

def retirer_carte():
    """
    permet de finir la session de l'utilisateur en lui demandant de recuperer sa carte
    """

    global carte_inseree

    chargement("Fermeture de votre session", 2)

    afficher("Veuillez récupérer votre carte.")

    carte_inseree = None

    afficher("Merci de votre visite !")
