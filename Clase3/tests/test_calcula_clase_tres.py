"""from Clase3.operaciones import suma, resta, multiplicacion, division
from Clase3.calcula_clase_tres import calcula
import pytest"""





"""1-Casos de prueba por operación Crea dos tests para cada función (sumar, restar, multiplicar, dividir):

Éxito : resultado correcto.

Error : comportamiento esperado ante fallo (p. ej. dividir debe lanzar ValueError al dividir por 0)"""
#suma con números positivos
"""def test_suma_positiva():
    assert suma(10, 2) == 12
    
    #suma con números negativos
def test_suma_negativos():
    assert suma(-10, -2) == -12  
    
    # resta con números positivos 
def test_resta_positivos():
    assert resta(10, 2) == 8    
    
    # resta con números negativos
def test_resta_negativos():
    assert resta(-10, -2) == -8
    
    # multiplicación con número positivo
def test_multiplicacion_positiva():
    assert multiplicacion(10, 2) == 20

    # multiplicación con número negativo
def test_multiplicacion_negativa():
    assert multiplicacion(-10, -2) == 20
    
    # división con número positivo
def test_division_positivo():
    assert division(10, 2) == 5
    
    # division con número negativo
def test_division_negativo():
    assert division(-10, -2) == 5
    
    # división por cero    
def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return num1 / num2
#dividir cero ortra forma"""
"""def test_division_cero():
    with pytest.raises(ValueError):
        division(10, 0)"""
        
from clase3.operaciones import suma, resta, multiplicacion, division
import pytest

"""1-Casos de prueba por operación
Crea dos tests para cada función (sumar, restar, multiplicar, dividir):

Éxito : resultado correcto.
Error : comportamiento esperado ante fallo (p. ej. dividir debe lanzar ZeroDivisionError al dividir por 0)
"""

# suma con números positivos
def test_suma_positiva():
    assert suma(10, 2) == 12

# suma con números negativos
def test_suma_negativos():
    assert suma(-10, -2) == -12

# resta con números positivos
def test_resta_positivos():
    assert resta(10, 2) == 8

# resta con números negativos
def test_resta_negativos():
    assert resta(-10, -2) == -8

# multiplicación con número positivo
def test_multiplicacion_positiva():
    assert multiplicacion(10, 2) == 20

# multiplicación con número negativo
def test_multiplicacion_negativa():
    assert multiplicacion(-10, -2) == 20

# división con número positivo
def test_division_positivo():
    assert division(10, 2) == 5

# división con número negativo
def test_division_negativo():
    assert division(-10, -2) == 5

# división por cero: debe lanzar ZeroDivisionError
def test_division_cero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)        