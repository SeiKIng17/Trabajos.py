print("Ingrese cuatro números:")
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Ordenar los números utilizando comparaciones
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num3 > num4:
    num3, num4 = num4, num3
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2

print("Los números ordenados son:", num1, num2, num3, num4)