import unittest

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

class TestDividir(unittest.TestCase):

    def test_dividir_prositivo(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_negativo(self):
        self.assertEqual(dividir(-10, 2), -5)

    def test_dividir_decimales(self):
        self.assertEqual(dividir(10, 4), 2.5)

    def test_dividir_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

class TestConexionDummy(unittest.TestCase):
    def setUp(self):
        print("\n[setUp] Conectando a la base de datos de pruebas...")
        self.conexion = "Conectado"

    def test_operacion_uno(self):
        self.assertEqual(self.conexion, "Conectado")

    def test_operacion_dos(self):
        self.assertTrue(self.conexion.startswith("Cone"))

    def tearDown(self):
        print("\n[tearDown] Cerrando la conexion de pruebas...")
        self.conexion = "Desconectado"

if __name__ == '__main__':
    unittest.main()