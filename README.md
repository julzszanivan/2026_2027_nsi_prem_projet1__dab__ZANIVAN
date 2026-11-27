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
2) verification du code pin avec donc trois essai possible si on echoue apres les 3, la carte est avaler et un message s'affiche puis on retourne à 1)
3) apres avoir rentrer le bon code le menue s'affiche avec 5 option :1 voir le solde, 2 retirer de l'argent, 3 quitter, 4 deposer et 5 voir l'historique des flux d'argent dans le compte
    3.1) si 1 est taper alors le solde s'affiche
    3.2) si 2 est taper alors 
