print("imagina que vas a comprar zapatos")
marca = input("¿que marca de tenis prefieres?: ")
modelo = input("¿que modelo de tenis prefieres?: ")
talla = input("¿que talla de tenis deseas?: ")
cantidad = input("¿cuantos pares de tenis quieres comprar?: ")
zapato = {
    "marca" : marca,
    "modelo" : modelo,
    "talla" : talla,
    "cantidad" : cantidad,
}
print(f"Estos son tus datos:\n{zapato}")
print("¿deseas corregir algún dato de los que proporcionaste?")
if input("si/no: ") == "si":
    corregir=input("\n1.Marca\n2.Modelo\n3.Talla\n4.Cantidad\nDe los datos que proporcionaste escribe el numero del que deseas corregir:  ")
    if corregir == "1":
        marca_corregida=input("¿cual es la marca que deseas?")
        zapato["marca"]=marca_corregida
        print(f"Estos son tus datos:\n{zapato}")
    if corregir == "2":
        marca_corregida=input("¿cual es el modelo que deseas?")
        zapato["modelo"]=marca_corregida
        print(f"Estos son tus datos:\n{zapato}")
    if corregir == "3":
        marca_corregida=input("¿cual es la talla que deseas?")
        zapato["talla"]=marca_corregida
        print(f"Estos son tus datos:\n{zapato}")
    if corregir == "4":
        marca_corregida=input("¿cual es la cantidad que deseas?")
        zapato["cantidad"]=marca_corregida
        print(f"Estos son tus datos:\n{zapato}")

