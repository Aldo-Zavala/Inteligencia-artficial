edad= int(input("pon tu edad: "))
if edad >= 1 and edad <= 18:
    print("eres menor de edad")
elif edad >= 18 and edad <=60:
    print("eres adulto")
elif edad >= 60 and edad <=75:
    print("eres adulto mayor")
elif edad >= 75 and edad <=120:
    print("eres anciano")
else :
    print("ya deberias de estar muerto")