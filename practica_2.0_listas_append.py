print("ingresa el nombre de 4 personas: ")#pedimos al usuario que ingrese 4 nombres
nombre1=input("escribe el primer nombre: ")
nombre2=input("escribe el segundo nombre: ")
nombre3=input("escribe el tercer nombre: ")
nombre4=input("escribe el cuarto nombre: ")
nombres=[nombre1,nombre2,nombre3,nombre4]#guardamos los nombres en la lista
print("¿deseas agregar otro nombre?")#hacemos una condicion a ver si el usuario desea agregar otro nombre
if input("escribe si o no: ") == "si":#si el usuario dice que si entonces le pedimos que ingrese el nombre extra
    nombre_extra=input("escribe el otro nombre: ")#captuira el nombre extra
    nombres.append(nombre_extra)
#si el usuario dice que no entonces no se agrega nada
print("los nombres son: ")
print(nombres)#mostramos los nombres capturados en la lista 
