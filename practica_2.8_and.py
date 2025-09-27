print("vas a poner 3 numeros cualesquiera y te mostrare diferentes comparacciones ")
numero_1 = int(input("escribe el primer numero: "))
numero_2 = int(input("escribe el segundo numero: "))
numero_3 = int(input("escribe el tercer numero: "))
numeros = {
    "a." : numero_1,
    "b." : numero_2,
    "c." : numero_3,

}
print(f"estos son los numeros que pusiste: {numeros}")
print("ahora te mostrare las diferentes comparaciones")
print("1. a < b y b > c")
print("2. a > b y b < c")
if input("selecciona cual delas dos opciones deseas ver: ") == "1":
    comparacion_1 = numero_1 < numero_2 and numero_2 > numero_3
    print(f"el resultado de la comparacion es: {comparacion_1}")
if input("selecciona cual delas dos opciones deseas ver: ") == "2":
    comparacion_2 = numero_1 > numero_2 and numero_2 < numero_3
    print(f"el resultado de la comparacion es: {comparacion_2}")