class CompteBancaire:
    def __init__(self,nomprenom,numéro,solde,code):
        self.__Nom_Prénom = nomprenom
        self.__numéro_compte = numéro
        self.__solde = solde
        self.__code = code
        
    
    def getNom_Prénom(self):
        return self.__Nom_Prénom
    def getnuméro(self):
        return self.__numéro_compte
    def setnuméro(self,numéro):
        self.__numéro_compte = numéro
    def getsolde(self):
        return self.__solde
    def setsolde(self,solde):
        self.__solde = solde
    def code(self):
        return self.__code
    
    def ModifierMP(self,newcode):
        self.__code = newcode

    def déposer(self,argent):
        self.__solde = self.__solde + argent
    def retirer_argent(self,argent):
        if (self.__solde < argent):
            print("impossible d'effectuer l'opération , solde insuffisant")
        else:
            self.__solde = self.__solde - argent
    def code_secret(self,numbre):
        if self.__code + numbre :
            if numbre > 0 and numbre < 100 :
              print("Pouvez-vous ouvrir votre compte . Mon code est :",self.__code + numbre)
            else: 
              print("vous ne pouvez pas ouvrir ce compte")
    def aficherInfo(self):
        print("le nom et le prénom de cette pérsonne est :",self.__Nom_Prénom)
        print("le numéro de compte est :",self.__numéro_compte)
        print("le solde dans votre compte est :",self.__solde)
        print("le code de votre compte est :",self.__code)
    def Ajouter_compte(self,nomprenom,numéro,solde,code):
        self.__Nom_Prénom = nomprenom
        self.__numéro_compte = numéro
        self.__solde = solde
        self.__code =code
    def supprimer_compte(self):
        print("supprimer ce compte de personne :",self.__Nom_Prénom)
    
monCompte = CompteBancaire("ali salhi",16168891,22300,7)
"""monCompte.aficherInfo()
monCompte.déposer(1500)
monCompte.retirer_argent(24000)
monCompte.code_secret(43)
monCompte.Ajouter_compte("sara sawri",21435697,34300,3)
monCompte.supprimer_compte()"""
monCompte.ModifierMP(3)