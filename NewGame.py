print("Mirsevini ne quiz")
ans=input("Deshironi te merrni pjese(po/jo)")
score=0
total_qs=6
if ans.lower()=="po":
    ans=input("Kush eshte kryeqyteti i Bullgarise: ")
    if ans.lower()=="sofia":
        score+=1
        print("E sakte")
    else:
        print("E pasakte")


    ans=input("Cili brand i telefonave krijon telefonat me te sigurt ne sistem: ")
    if ans.lower()=="apple" or ans.lower()=="iphone":
        score+=1
        print("E sakte")
    else:
        print("E pasakte")


    ans=input("Sa eshte vlera e permbledhur trefishor e numrit pi: ")
    if ans.lower()=="3.14":
        score+=1
        print("E sakte")
    else:
        print("E pasakte")


    ans=input("Kush e zbuloi penicilinen: ")
    if ans.lower()=="aleksander Flamingu" or ans.lower()=="flamingu":
        score+=1
        print("E sakte")
    else:
        print("E pasakte")


    ans=input("8+3*12/9")
    if ans.lower()=="12":
        score+=1
        print("E sakte")
    else:
        print("E pasakte")

    
    ans=input("Kush e luan rolin e Tony Montana ne filmin Scarface: ")
    if ans.lower()=="al pacino" or ans.lower()=="alpacino":
        score+=1
        print("E sakte")
    else:
        print("E pasakte")

    print("Faleminderit qe luajtet, ju keni",score,"pergjigje te sakta")
    perqindja=score/total_qs*100
    print("perqindja:",str(perqindja)+"%")

elif ans.lower()=="jo":
    print("Tung")