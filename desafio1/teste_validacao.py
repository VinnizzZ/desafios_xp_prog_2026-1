import validacoes
import unittest

class TestEmail(unittest.TestCase):

    def test_email_valido1(self):
        self.assertTrue(validacoes.ehEmailValido('email@email.com'))

    def test_email_valido2(self):
        self.assertTrue(validacoes.ehEmailValido('emailteste@hotmail.com'))

    def test_email_pontobr(self):
        self.assertTrue(validacoes.ehEmailValido('email@email.com.br'))

    def test_email_invalido1(self):
        self.assertFalse(validacoes.ehEmailValido('email@email'))

    def test_email_invalido2(self):
        self.assertFalse(validacoes.ehEmailValido('email.com'))

class TestCPF(unittest.TestCase):

    def test_CPF_valido1(self):
        self.assertTrue(validacoes.ehCPFValido('123.456.789-10'))

    def test_CPF_valido2(self):
        self.assertTrue(validacoes.ehCPFValido('098.765.432-12'))

    def test_CPF_semPonto(self):
        self.assertFalse(validacoes.ehCPFValido('123456789-10'))

    def test_CPF_semTraco(self):
        self.assertFalse(validacoes.ehCPFValido('123.456.78910'))

    def test_CPF_invalido(self):
        self.assertFalse(validacoes.ehCPFValido('12345'))

class TestSenha(unittest.TestCase):

    def test_Senha_valido1(self):
        self.assertTrue(validacoes.ehSenhaForte('aA12345678!'))

    def test_Senha_valido2(self):
        self.assertTrue(validacoes.ehSenhaForte('Senha123!'))

    def test_Senha_pequena(self):
        self.assertFalse(validacoes.ehSenhaForte('7letras'))

    def test_Senha_semNumero(self):
        self.assertFalse(validacoes.ehSenhaForte('Senhasemnumero!'))

    def test_Senha_semEspecial(self):
        self.assertFalse(validacoes.ehSenhaForte('53Nh453m35p3c141'))

if __name__ == '__main__':
    unittest.main()