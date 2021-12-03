nom=input("entrez votre nom")
prenom=input("entrez votre prenom")
age=int(input("entrez votre age"))

if age >= 18 :
    print(nom,prenom,age,"majeure")
else:
    print(nom,prenom,age,"mineure")
