
User1="hmayorga";
Contra1="1234" ;
User2="gomez";
Contra2="gomez123";

UserPrendido=False;
Sistema=False;

while UserPrendido==False :
    UserCont=False;  UserNom=False;
    print ("======================Servicio de Fotocopiado===================================");
    userNomCont=str(input("Ingresa tu nombre de usuario=\n"))
    if userNomCont==User1 or userNomCont==User2 : 
        UserConCont=str(input("Ingresa tu contraseña=\n"))
        if userNomCont==User1 and UserConCont==Contra1 :
            UserCont=True; 
            UserNom=True;
        elif userNomCont==User2 and UserConCont==Contra2 :
             UserCont=True;
             UserNom=True;
    if UserCont==True and UserNom==True :
        UserPrendido=True;
        Sistema=True;
        print("Bienvenido al sistema");
    elif UserCont==False or UserNom==False :
        print("Usuario o contraseña erroneo");