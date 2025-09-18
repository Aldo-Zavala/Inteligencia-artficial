#en este codigo sacaremos el promedio de 10 materias 
calificaciones = [100,90,85,78,70,90,95,82,85,60]
#en esta parte sumaremos todas las califiacaciones 
suma_calificaciones = sum(calificaciones)
#en esta parte del codigo se contaran la cantidad de calificaciones que hay
numero_calificaciones = len(calificaciones)
#calulamos el promedio de estas calificaciones
promedio = suma_calificaciones/numero_calificaciones
print("Tus calificaciones son: \n100\n90\n85\n78\n70\n90\n95\n82\n85\n60")#mostramos las calificaiones declaradas en la variable calificaciones
print("El numero de materias es: ",numero_calificaciones)#mostramos la cantidad de calificaciones que hay 
print("El promedio total es ; ",promedio)#mostramos el promedio de las calificaciones