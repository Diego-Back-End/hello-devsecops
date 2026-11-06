import unittest

from app import saludo


class TestSaludo(unittest.TestCase):
    def test_saludo_por_defecto(self):
        self.assertEqual(saludo(), "Hola, Mundo!")

    def test_saludo_con_nombre(self):
        self.assertEqual(saludo("Diego"), "Hola, Diego!")


if __name__ == "__main__":
    unittest.main()
