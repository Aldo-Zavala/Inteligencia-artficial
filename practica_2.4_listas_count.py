print("Capturaras 8 calificaciones en una lista ")#le pedimos al usuario que capture 8 calificaciones
calificacion1 = input("calificacion 1: ")
calificacion2 = input("calificacion 2: ")
calificacion3 = input("calificacion 3: ")
calificacion4 = input("calificacion 4: ")
calificacion5 = input("calificacion 5: ")
calificacion6 = input("calificacion 6: ")
calificacion7 = input("calificacion 7: ")
calificacion8 = input("calificacion 8: ")
calificaciones=[calificacion1,calificacion2,calificacion3,calificacion4,calificacion5,calificacion6,calificacion7,calificacion8]#creamos una lista
print("deseas buscar una calificacion en la lista")
if input("si/no:") == "si":#creamos una condicion para ver si el usuario desea buscar una calificacion
    calificacion_buscar = input("pon la calificacion que seas buscar: ")#capturamos la calificacion a buscar
    print(calificaciones)
    if calificacion_buscar not in calificacion1 and calificacion_buscar not in calificacion2 and calificacion_buscar not in calificacion3 and calificacion_buscar not in calificacion4 and calificacion_buscar not in calificacion5 and calificacion_buscar not in calificacion6 and calificacion_buscar not in calificacion7 and calificacion_buscar not in calificacion8:
        print("la calificacion no se encuentra en la lista")
    else:
       coincidencias = calificaciones.count(calificacion_buscar)
       print(f"la calificacion {calificacion_buscar} hay {coincidencias} veces")

