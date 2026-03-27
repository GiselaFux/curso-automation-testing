"""Pytest

1-Casos de prueba por operación Crea dos tests para cada función (sumar, restar, multiplicar, dividir):

Éxito : resultado correcto.

Error : comportamiento esperado ante fallo (p. ej. dividir debe lanzar ValueError al dividir por 0)

2-Fixtures

Conserva el fixture de enteros existente.

Añade un segundo fixture con valores flotantes (0.1, 0.2) y utilízalo donde corresponda.

Markers

3-ParametrizaciónPara sumar y restar, usa 
Etiqueta los tests de sumar con @pytest.mark.smoke.

Etiqueta los tests de dividir que validan la excepción con @pytest.mark.exception.

4-Muestra cómo filtrar la ejecución:

pytest -m smoke        # solo tests “sumar”

pytest -m exception    # solo tests “dividir” con error

5-Reporte HTML

Genera el informe con: pytest --html=report.html.

Sube report.html junto con tu Pull Request.
"""
import pytest
from calculadora import suma, resta, multiplicacion, division


# ---------- FIXTURES ----------

@pytest.fixture
def enteros_positivos():
    return 10, 2   # ejemplo de enteros


@pytest.fixture
def flotantes():
    return 0.1, 0.2  # ejemplo flotantes


# ---------- SUMA (parametrización + smoke) ----------

@pytest.mark.smoke
@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (1, 2, 3),       # enteros positivos
        (-2, -10, -12),  # enteros negativos
        (0, 0, 0),       # ceros
    ],
)
def test_suma_parametrizada(a, b, esperado):
    assert suma(a, b) == esperado


@pytest.mark.smoke
def test_suma_float(flotantes):
    a, b = flotantes
    # flotantes → 0.1 + 0.2 = 0.30000000000000004, usamos approx para comparar con margen de error
    assert suma(a, b) == pytest.approx(0.3)


@pytest.mark.smoke
def test_suma_smoke(enteros_positivos):
    a, b = enteros_positivos
    assert suma(a, b) == 12


@pytest.mark.smoke
def test_suma_smoke_float(flotantes):
    a, b = flotantes
    assert suma(a, b) == pytest.approx(0.3)


# ---------- RESTA (parametrización) ----------

@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (10, 2, 8),      # enteros positivos
        (-1, -2, 1),     # enteros negativos
        (0, 0, 0),       # ceros
    ],
)
def test_resta_parametrizada(a, b, esperado):
    assert resta(a, b) == esperado


def test_resta_parametrizada_float(flotantes):
    a, b = flotantes
    assert resta(a, b) == pytest.approx(-0.1)


# ---------- MULTIPLICACIÓN (éxito + caso positivo negativo) ----------

def test_multiplicacion_exito(enteros_positivos):
    a, b = enteros_positivos
    assert multiplicacion(a, b) == 20


def test_multiplicacion_negativa():
    assert multiplicacion(-10, -2) == 20


# ---------- DIVISIÓN (éxito + error con excepción) ----------

def test_division_exito(enteros_positivos):
    a, b = enteros_positivos
    assert division(a, b) == 5


@pytest.mark.exception
def test_division_cero():
    with pytest.raises(ValueError):
        division(10, 0)
