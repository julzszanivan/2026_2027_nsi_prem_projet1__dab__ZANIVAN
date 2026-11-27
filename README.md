# 2026_2027_nsi_prem_project1__dab
dab ( distributeur automatique de billet)

theo leluc
sienna manchec
jules zanivan

la repartition des tache: Théo: compte_bancaire_identification + programme_principale+ verification d'identité+ retirer carte
                         sienna: depot + retrait billets+ chargement et autre effet visuels
                         jule : menu et creer un compte
C'est a titre indicatif, on avait en gros cette répartition au début mais on a aussi travaille sur les codes des autres comme on peut voir dans l'historique du projet sur github

mode d'emploi: 
1) mettre 0(si pas de compte) ou 1 (si on a deja un compte)
    1.1)si pas de compte alors on demande de taper une somme a mettre dans la carte puis les information de la carte avec le solde donner, le numéro de carte et le code pin fait aléatoirement, le plafon qui est de 500 pour tous les comptes creer
    1.2)si deja un compte alors il faut rentrer le numero de carte dans la machine qui représente le moment ou on insere la carte
    1.3) si on tape un code qui n'existe pas alors un message d'erreur apparait et on retourne à 1)
2) verification du code pin avec donc trois essai possible si on echoue apres les 3, la carte est avaler et un message s'affiche puis on retourne à 1)
3) apres avoir rentrer le bon code le menue s'affiche avec 5 option :1 voir le solde, 2 retirer de l'argent, 3 quitter, 4 l'historique des flux d'argent dans le compte et 5 deposer de l'argent
    3.1) si 1 est taper alors le solde s'affiche
    3.2) si 2 est taper alors on doit mettre le montant qu'on veut enlever
        3.2.1) si le montant de passe le solde ou le plafon alors un message indicant cela sera afficher et il faudra remettre un chiffre plus petit
        3.2.2) sinon le montant est donner avec le minimum de billet possible et le solde et le plafon sont actualise et on retourne sur le 3)
    3.3) si on tape 3 alors on se déconnecte et on reprend sa carte et le programme retourne sur 1)
    3.4) si on tape 4 alors on peut voir l'historique des flux d'agent dans le compte
    3.5) si on tape 5 alors on peut déposer de l'argent
        3.5.1) si on entre autre chose que des nombre divisible par 10 alors le programme demandera de mettre des nombres divisible par 10
        3.5.2) sinon il y aura une animation pour verifier les billets puis le solde sera actualiser et donne au client
    3.6) si on rentre autre chose alors le programme demande d'entrer un chiffre entre 1 et 5
    3.7) si on prend plus 15 secondes a repondre alors une verification d'identité apparaitra avec une erreur possible sur le code pin
        3.7.1) si le code est bon alors le code continue en fonction de ce que vous avez taper dans le menu
        3.7.2) si le code n'est pas bon alors un message indiquant que la carte est avaler apparait et un envoie de message a l'utilisateur est envoyer pour prévenir ue sa carte est en sécurité a la banque puis le programme retourne sur 1)
