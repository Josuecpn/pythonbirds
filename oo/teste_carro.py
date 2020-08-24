from unittest import TestCase
from carro import Motor

class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()

        self.assertEqual(0, motor.velocidade)
