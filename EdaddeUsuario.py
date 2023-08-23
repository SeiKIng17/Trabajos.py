from time import localtime
t = localtime()
dia = t.tm_mday
mes = t.tm_mon
anno = t.tm_year

# Solicitar el día de nacimiento
dia_nacimiento = int(input("Ingrese su día de nacimiento: "))
# Solicitar el mes de nacimiento
mes_nacimiento = int(input("Ingrese su mes de nacimiento: "))
# Solicitar el año de nacimiento
anno_nacimiento = int(input("Ingrese su año de nacimiento: "))

# Obtener la fecha actual
fecha_actual = localtime()

# Calcular la edad
edad = fecha_actual.tm_year - anno_nacimiento
# Ajustar la edad si el cumpleaños aún no ha ocurrido este año
if (mes_nacimiento, dia_nacimiento) > (fecha_actual.tm_mon, fecha_actual.tm_mday):
    edad -= 1

print("Usted tiene", edad, "años")
