def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Error: No se puede dividir por cero")
    return num1 / num2

