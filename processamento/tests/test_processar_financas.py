try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
# from processar_financas import enviar_notas_fiscais, enviar_debitos
from processar_financas import enviar_notas_fiscais, enviar_debitos


class TestEnviarFinancas(unittest.TestCase):
    def test_enviar_notas_fiscais_exemplo_instrucoes_desafio(self):
        indice = 50
        nfs = 3
        saida = 53
        self.assertEqual(
            enviar_notas_fiscais(nfs, indice), saida,
            msg=f'não retornou "{saida}"',
        )

    def test_enviar_notas_fiscais_deve_retornar_int(self):
        indice = 50
        nfs = [x for x in range(10)]

        for nf in nfs:
            with self.subTest(nf=nf, indice=indice):
                self.assertIsInstance(
                    enviar_notas_fiscais(nf, indice), int,
                    msg='não retornou "int"',
                )

    def test_enviar_notas_fiscais_deve_retornar_100_quando_indice_for_maior_que_100(self):
        indice = 100
        nfs = [x for x in range(10)]

        for nf in nfs:
            with self.subTest(nf=nf, indice=indice):
                self.assertEqual(
                    enviar_notas_fiscais(nf, indice), 100,
                    msg='não retornou "100"',
                )

    def test_enviar_debitos_exemplo_instrucoes_desafio(self):
        indice = 53
        ds = 1
        saida = 51
        self.assertEqual(
            enviar_debitos(ds, indice), saida,
            msg=f'não retornou "{saida}"',
        )

    def test_enviar_debitos_deve_retornar_int(self):
        indice = 50
        ds = [x for x in range(10)]

        for d in ds:
            with self.subTest(d=d, indice=indice):
                self.assertIsInstance(
                    enviar_debitos(d, indice), int,
                    msg='não retornou "int"',
                )

    def test_enviar_debitos_deve_retornar_1_quando_indice_for_menor_que_1(self):
        indice = 1
        ds = [x for x in range(10)]

        for d in ds:
            with self.subTest(d=d, indice=indice):
                self.assertEqual(
                    enviar_debitos(d, indice), 1,
                    msg='não retornou "1"',
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)
