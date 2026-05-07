import legacy
import unittest

class TestProcessar(unittest.TestCase):

    def test_vip_maior_que_500(self):
        self.assertEqual(legacy.processar(550, 'VIP'), 550*.8)

    def test_vip_500(self):
        self.assertEqual(legacy.processar(500, 'VIP'), 500*.9)

    def test_vip_menor_que_500(self):
        self.assertEqual(legacy.processar(490, 'VIP'), 490*.9)

    def test_not_vip_maior_que_500(self):
        self.assertEqual(legacy.processar(550, 'not_VIP'), 550*.95)

    def test_not_vip_500(self):
        self.assertEqual(legacy.processar(500, 'not_VIP'), 500)

    def test_not_vip_menor_que_500(self):
        self.assertEqual(legacy.processar(490, 'not_VIP'), 490)

    def test_vip_lowercase(self):
        self.assertEqual(legacy.processar(500, 'vip'), 500)

class TestFormatar(unittest.TestCase):

    def test_valor_sem_centavos(self):
        self.assertEqual(legacy.formatar(20), 'R$20.00')

    def test_valor_centavos(self):
        self.assertEqual(legacy.formatar(20.00), 'R$20.00')

    def test_valor_varios_decimais(self):
        self.assertEqual(legacy.formatar(20.0000000000000000), 'R$20.00')

    def test_valor_invalido(self):
        with self.assertRaises(ValueError):
            legacy.formatar('20.00')

if __name__ == '__main__':
    unittest.main()