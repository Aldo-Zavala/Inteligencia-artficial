nombres = {"Aldo","Juan","Pedro","Maria"}#creamos un set con nombres
print(nombres)#mostramos los nombres
print("deseas eliminar algun nombre? si/no")#preguntamos si desea eliminar algun nombre
if input()=="si":
    quitar = input("escribe el nombre que seas eliminar: ")
    if quitar not in nombres:
        print("nombre no encontrado")#si el nombre no se encuentra en el set mostramos este mensaje
    else:
        nombres.discard(quitar)#eliminamos el nombre que el usuario escribio
        print("aqui esta ya corregido")#mostramos este mensaje
        print(nombres)#mostramos el set ya corregido