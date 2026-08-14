import pytest

def suma(a, b):
    return a + b

def test_sumar_enteros():
    assert suma(2, 3) == 5

def test_sumar_decimales():
    assert suma(2.5, 3.5) == 6.0

def test_sumar_negativos():
    assert suma(-2, -3) == -5

def es_par(numero):
    return numero % 2 == 0

@pytest.fixture
def usuario_ejemplo():
    print("\n[Fixture] Creando usuario de prueba")
    return {"nombre": "Santiago", "rol": "admin"}

def test_usuario_nombre(usuario_ejemplo):
    assert usuario_ejemplo["nombre"] == "Santiago"

def test_usuario_rol(usuario_ejemplo):
    assert usuario_ejemplo["rol"] == "admin"

@pytest.mark.parametrize("entrada, esperado", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (-5, False)
])

def test_es_par(entrada, esperado):
    assert es_par(entrada) == esperado
