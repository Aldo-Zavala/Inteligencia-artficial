print("ingresa el nombre de 4 personas: ")#capturamos el nombre de 4 personas
nombre1=input("escribe el primer nombre: ")
nombre2=input("escribe el segundo nombre: ")
nombre3=input("escribe el tercer nombre: ")
nombre4=input("escribe el cuarto nombre: ")
lista_nombres=[nombre1,nombre2,nombre3,nombre4]#guardamos los 4 nombres en la lista
print(lista_nombres)# mostramos la lista de nombres capturados para que el usuario pueda ver los nombres
print("¿deseas eliminar un nombre de la lista ?")
if input("escribe si o no: ")== "si":
    eliminar=input("escribe el nombre capturado que desees eliminar:  ")#creamos la variable eliminar para capturar el nombre que el usuario desea eliminar
    lista_nombres.remove(eliminar)#usamos remove para eliminar el nombre capturado
    print("aqui esta la lista ya corregida:")
    print(lista_nombres)
