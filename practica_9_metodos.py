nombre= input("Escibe tu nombre (en minusculas): ")#declaramos variable nombre para capturar el nombre del usuario
apellido= input("Escibe tu apellido (en minusculas): ")#declaramos variable apellido para capturar el apellido del usuario
nombre_M=input("Escibe otra vez tu nombre (en mayusculas): ")#declaramos variable nombre_M para capturar el nombre del usuario escrito en mayusculas
appelido_M=input("Escibe otra vez tu apellido (en mayusculas): ")#declaramos variable apellido_M para capturar el apellido del usuario escrito en mayusculas
nombre_capitalize= nombre.capitalize() #declaramos esta variable para usar el metodo capitalize con el nombre del usuario
apellido_capitalize= apellido.capitalize()#declaramos esta variable para usar el metodo capitalize con el apellido del usuario
nombre_upper= nombre.upper()#declaramos esta variable para usar el metodo upper con el nombre del usuario
apellido_upper= apellido.upper()#declaramos esta variable para usar el metodo upper con el apellido del usuario
nombre_lower= nombre_M.lower()#declaramos esta variable para usar el metodo lower con el nombre del usuario es crito en mayusculas
apellido_lower= appelido_M.lower()#declaramos esta variable para usar el metodo lower con el apellido del usuario es crito en mayusculas
print(f"Tu nombre escrito con el metodo capitalize: {nombre_capitalize} {apellido_capitalize}")
print(f"Tu nombre escrito con el metodo upper: {nombre_upper} {apellido_upper}")
print(f"Tu nombre escrito con el metodo lower: {nombre_lower} {apellido_lower}")

