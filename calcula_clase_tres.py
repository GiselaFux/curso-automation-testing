"""Clase 3:Actividad 1: Mejorando la calculadora
Refactorizar el script de la calculadora lineal en al menos 4 funciones separadas. una por cada tipo de operación.
Como ser: Sumar(), Restar(), Multiplicar() y Dividir()
Añadir manejo de excepciones para entradas inválidas y división por cero."""



  
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero"
    return num1 / num2

def calculadora(operacion, num1_str, num2_str):  # Renombré para claridad
    
    num1_str = input("Ingresa tu primer número: ")
    num2_str = input("Ingresa el segundo número: ")
    operacion = input("Ingresa una operaciön( Elige entre + , - , * , / ):  ")
    try:
        # Convierte inputs ANTES del if
        num1 = float(num1_str)
        num2 = float(num2_str)
        
        # Ahora usa parámetros convertidos
        if operacion == "+":
            return suma(num1, num2)
        elif operacion == "-":
            return resta(num1, num2)
        elif operacion == "*":
            return multiplicacion(num1, num2)
        elif operacion == "/":
            return division(num1, num2)
        else:
            return "Error: Operación no válida"
            
    except ValueError:
        return "Error: Ingresa números válidos (ej: 5, 10.5)"
    except Exception as e:
        return f"Error inesperado: {e}"
    finally:
        print("Cálculo procesado")


# ✅ Uso correcto (pasa strings)
print(calculadora("+", "5", "3"))      # 8.0
print(calculadora("/", "10", "0"))     # Error: No se puede dividir por cero
print(calculadora("+", "abc", "5"))    # Error: Ingresa números válidos (ej: 5, 10, 5.5)
