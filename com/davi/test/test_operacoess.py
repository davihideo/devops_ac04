from unittest import TestCase
from com.davi.operacoess import Operacoes

class TestOperacoes(TestCase):

	def setUp(self):
		self.operacoes = Operacoes()
		
	def test_multiplicacao(self):
		self.assertEqual(self.operacoes.multiplicacao([1,5]), 25, "Should be 25")
		
	def test_divisao(self):
		self.assertEqual(self.operacoes.divisao([1,2]), 5, "Should be 5")