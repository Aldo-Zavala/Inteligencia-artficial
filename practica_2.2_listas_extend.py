print("ingresa el nombre de 4 personas: ")#capturamos el nombre de 4 personas
nombre1=input("escribe el primer nombre: ")
nombre2=input("escribe el segundo nombre: ")
nombre3=input("escribe el tercer nombre: ")
nombre4=input("escribe el cuarto nombre: ")
lista_1=[nombre1,nombre2,nombre3,nombre4]#guardamos los 4 nombres en la lista
print("deseas agregar otra lista de 4 nombres?")
if input("escribe si o no:  ") == "si":#creamos una condicion para ver si el usuario desea agregar otra lista 
    nombre5=input("escribe el otro primer nombre: ")
    nombre6=input("escribe el otro segundo nombre: ")
    nombre7=input("escribe el otro tercer nombre: ")
    nombre8=input("escribe el otro cuarto nombre: ")
    lista_2=[nombre5,nombre6,nombre7,nombre8]#capturamos la segunda lista
    lista_1.extend(lista_2)#usamos extend para unir las dos listas
    print("los nombres juntos son: ")
    print(lista_1)#mostramos las dos listas juntas
else:#si el usuario dice que no entonces mostramos los datos de la lista capturada
    print("ok, no se agregara otra lista")
    print("los nombres capturados son: ")
    print(lista_1)
