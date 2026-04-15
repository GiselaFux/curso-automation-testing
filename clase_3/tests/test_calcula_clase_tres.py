import pytest

from clase_3.operaciones import suma, resta, multiplicacion, division
from clase_3.calcula_clase_tres import calcula        


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