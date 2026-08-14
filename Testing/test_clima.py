import unittest
from unittest.mock import Mock, patch
import requests

def obtener_temperatura_ciudad(ciudad):
    respuesta = requests.get(f"https://api.clima.com/{ciudad}")
    datos = respuesta.json()
    return datos["temperatura"]

# Patch y Mock

class TestClima(unittest.TestCase):
    @patch("requests.get")
    def test_obtener_temperatura_ciudad(self, mock_get):
        mock_respuesta = Mock()
        mock_respuesta.json.return_value = {"temperatura": 25}
        mock_get.return_value = mock_respuesta

        temperatura = obtener_temperatura_ciudad("Madrid")

        self.assertEqual(temperatura, 25)
        mock_get.assert_called_once_with("https://api.clima.com/Madrid")

if __name__ == "__main__":
    unittest.main()