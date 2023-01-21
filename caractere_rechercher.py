
chaines = "hcgshqokisbniuyttuzkz,huioiu"
lettre_deja_compter=[]
compter = True
i = 0

for lettre in chaines: #prendre une lettre dans notre chaine de caractere
    #lettre existe t'elle dans lettre_deja_compter
    while i <= len(lettre_deja_compter):
        if lettre != lettre_deja_compter[i]:
            compter = False
        else:
            compter = True
        i= i + 1

    if compter == False:
        #on compte le nombre de fois que notre lettre est repété
        print(f"la {lettre} est repete {chaines.count(lettre)}")
        #on ajoute lettre dans notre liste lettre_deja_compter
        lettre_deja_compter.append(lettre)
    

   
    
    