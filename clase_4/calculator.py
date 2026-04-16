

from clase_4.operations import suma, resta, multiplicacion, division




def calculador(operacion, num1_str, num2_str):
    # OJO: si vas a usar los parámetros, no los pises con input().
    # Si querés que pida por consola, lo correcto es NO tener parámetros.
    num1_str = input("Ingresa tu primer número: ")
    num2_str = input("Ingresa el segundo número: ")
    operacion = input("Ingresa una operación (Elige entre + , - , * , /): ")

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
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            return division(num1, num2)
        else:
            return "Error: Operación no válida"

    except ValueError as e:
        # Aquí mezclas ValueError de número inválido y de división por cero
        return f"Error: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"
    finally:
        print("Cálculo procesado")


# ⚠ Para usar pytest, es mejor NO ejecutar lógica al importar el módulo.
# Coméntalo o protégelo con if __name__ == "__main__":
if __name__ == "__main__":
    print(calculador("+", "5", "3"))
    print(calculador("/", "10", "0"))
    print(calculador("+", "abc", "5"))