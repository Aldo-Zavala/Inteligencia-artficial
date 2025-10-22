print("Del siguiente menu selecciona una opcion de lo que quieres que haga el programa\n\n")
menu=input("1.Saludo\n2.Captura tu nombre\n3.Captura tu edad\n  opcion: ")
match menu:
    case "1":
        print("Hola, espero que estes teniendo un buen dia")
    case "2":
        nombre=input("¿Cual es tu nombre?: ")
        print(f"Mucho gusto {nombre}, espero que tengas un buen dia")
    case "3":
        edad=int(input("¿Cual es tu edad?: "))
        print(f"Ah, tienes {edad} años, espero que tengas un buen dia")
    case _: 
        print("Opcion no valida, por favor selecciona una opcion del menu")    