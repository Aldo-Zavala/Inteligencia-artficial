print("ingresa el nombre de 4 personas: ")#capturamos el nombre de 4 personas
nombre1=input("escribe el primer nombre: ")
nombre2=input("escribe el segundo nombre: ")
nombre3=input("escribe el tercer nombre: ")
nombre4=input("escribe el cuarto nombre: ")
nombres=[nombre1,nombre2,nombre3,nombre4]#guardamos los 4 nombres en la lista 
print("¿deseas agregar otro nombre a la lista ?")
if input("escribe si o no:  ") == "si":#creamos una condicion para ver si el usuario desea agregar otro nombre
    nombre_extra=input("escribe el otro nombre: ")#si el usuario dice que si entonces capturamos el nombre extra
    i=int(input("escribe la posicion donde quiers agrgar el nombre (0,1,2,3,4): "))#el usuario decide en que posicion coloca el nombre 
    if i in [0,1,2,3,4]:#aqui escoge donqde lo quiere poner
        nombres.insert(i,nombre_extra)#cpturamos la posicion 
    else: print("posicion no valida")#si el usuario ingresa una posicion que no es valida entonces le decimos que no es valida
        
print("los nombres son: ")
print(nombres)#mostramos los nombres capturados en la lista


