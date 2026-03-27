# clase 1 lunes 16-3-26

print("¡Hola Automation Tester!")

# clase 2 

""" Ejercicio 1   
Define variables para almacenar el nombre, edad y profesión del usuario.

Solicita estos datos por teclado utilizando input().

Imprime en pantalla un mensaje personalizado incluyendo todos estos datos."""

nombre = input("Escribe tu nombre: ")
print("Su nombre es: " + nombre) 
edad = input("Escribe tu edad: ")
print("su edad es de " + edad) 
profesion = input("Escribe tu profesión: ")
print("y su profesión es " + profesion)
print("Su nombre es: " + nombre + " su edad es de " + edad + " y su profesión es " + profesion)





""" Actividad 2:

Escribe un pequeño script que utilice un bucle para mostrar los primeros 10 números pares.

Usa condicionales para validar y mostrar sólo los números pares."""
"""# Mostrar los primeros 10 números pares
for numero in range(1, 21):  # Hasta 20 para obtener exactamente 10 pares
    if numero % 2 == 0:
        print(numero, end=" ")  # end=" " evita saltos de línea

print(numero, end=" ") """ # Nueva línea al final


#con while  

number = 1
pairNumber = 0

while pairNumber < 10:
    if number % 2 == 0:
        print(number, end=" ")  # Imprime EL PAR, no el contador
        pairNumber += 1         # Corrige: pairNumber (no pairNumero)
    number += 1                 # Mueve FUERA del if (siempre avanza)

print()  # Línea final

#calculadora con funciones SIMPLE UNIDAD 2

def calculador():
    num1 = float(input("Ingresa tu primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa una operacion(Elige entre + , - , * , / ):  ")

     # ← TODO ESTO MISMO NIVEL (4 espacios)
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 == 0:
            resultado = "Error: No ÷0"
        else:
            resultado = num1 / num2
    else:
        resultado = "Error operación"
    
    print(f"Resultado: {resultado}")

calculador()  # ← LLAMA función
