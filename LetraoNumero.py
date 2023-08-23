#Algoritmo para saber si es una letra o un numero
LetraoNumero = input("Ingrese un carácter: ")

# Verificar si es una letra (mayúscula o minúscula)
if 'a' <= LetraoNumero <= 'z' or 'A' <= LetraoNumero <= 'Z':
    print("Es una letra.")
# Verificar si es un número
elif '0' <= LetraoNumero <= '9':
    while True:
        siguiente_caracter = input("Ingrese el siguiente carácter o presione Enter para terminar: ")
        if siguiente_caracter == '':
            break
        elif '0' <= siguiente_caracter <= '9':
            LetraoNumero += siguiente_caracter
        else:
            print("No es un número válido.")
    print("Es un número:", LetraoNumero)
else:
    print("No es ni una letra ni un número.")


