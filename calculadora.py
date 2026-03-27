
def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        #return "Error: No se puede dividir por cero"
        raise ValueError("Error: No se puede dividir por cero")
    return num1 / num2


# FUNCION PURA: usa parámetros, no input()
def calculadora(operacion, num1_str, num2_str):
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)

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


# BLOQUE INTERACTIVO (solo se ejecuta si corres calculadora.py directamente)
if __name__ == "__main__":
    operacion = input("Ingresa una operación (elige entre + , - , * , /): ")
    num1_str = input("Ingresa tu primer número: ")
    num2_str = input("Ingresa el segundo número: ")

    resultado = calculadora(operacion, num1_str, num2_str)
    print("Resultado:", resultado)
