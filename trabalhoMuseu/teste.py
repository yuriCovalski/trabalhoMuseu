from unittest import TestCase
import alheios, locais, admin, artes


class testeMuseu(TestCase):

    def test_deve_atualizar_artigo_arni(self):
        artigo = artes.Artigo('ARNI', 'titulo da obra', alheios.date(2022, 12, 3), 'é uma arte')
        artigo.atualizaDocumentacao(ARNI='ARNINOVO')
        self.assertEqual(artigo.arni, 'ARNINOVO')

    def test_deve_atualizar_artigo_titulo(self):
        artigo = artes.Artigo('ARNI', 'titulo da obra', alheios.date(2022, 12, 3), 'é uma arte')
        artigo.atualizaDocumentacao(titulo='titulo')
        self.assertEqual(artigo.titulo, 'titulo')

    def test_deve_atualizar_artefato_aorni(self):
        artefato = artes.Artefatos('AORNI', 'titulo do artefato', alheios.date(2022, 12, 3), 'é uma arte')
        artefato.atualizaDocumentacao(AORNI='AORNINOVO')
        self.assertEqual(artefato.aorni, 'AORNINOVO')

    def test_deve_atualizar_artefato_descricao(self):
        artefato = artes.Artefatos('AORNI', 'titulo do artefato', alheios.date(2022, 12, 3), 'é uma arte')
        artefato.atualizaDocumentacao(descricao='nova descricao')
        self.assertEqual(artefato.descricao, 'nova descricao')

    def test_artista_deve_publicar_uma_arte(self):
        artista = artes.Artista('Yui', '104.890.279-90')
        artigo = artes.Artigo('ARNIYURI', 'titulo ARNIYURI', alheios.date(2022, 3, 12), 'é uma arte')
        artista.publica_arte(artigo)
        self.assertEqual(artista.lista_artes[0], artigo)

    def test_artista_deve_publicar_duas_artes(self):
        artista = artes.Artista('Yui', '104.890.279-90')
        artigo = artes.Artigo('ARNIYURI', 'titulo ARNIYURI', alheios.date(2022, 3, 12), 'é uma arte')
        artista.publica_arte(artigo)
        artigo_novo = artes.Artigo('ARNIYURI2', 'titulo ARNIYURI2', alheios.date(2022, 3, 13), 'é uma arte 2')
        artista.publica_arte(artigo_novo)
        self.assertEqual(artista.lista_artes[0], artigo)
        self.assertEqual(artista.lista_artes[1], artigo_novo)

    def test_artista_deve_fazer_evento(self):
        artista = artes.Artista('Yui', '104.890.279-90')
        evento = artista.faz_evento('evento', 'dia 14', '12 horas', locais.Local('parque'))
        self.assertEqual(evento, f'Evento feito com sucesso, data: dia 14 ás 12 horas.')

    def test_evento_deve_retornar_numero_da_plateia(self):
        numeroPlateia = alheios.randrange(1000)
        plateia = alheios.Plateia(numeroPlateia)
        evento = admin.Evento('Evento', alheios.date(2022, 12, 3), alheios.time(12), locais.Local('Bloco 1'))
        self.assertEqual(evento.numeroPlateia(plateia), numeroPlateia)

    def test_evento_deve_conter_local(self):
        evento = admin.Evento('casa de jogos', alheios.date(2022, 12, 3), alheios.time(12), 'casa')
        self.assertNotIsInstance(evento.local, locais.Local)

        evento = admin.Evento('casa de jogos', alheios.date(2022, 12, 3), alheios.time(12), locais.Local('casa'))
        self.assertIsInstance(evento.local, locais.Local)

    def test_deve_dar_erro_verba_negativa(self):
        with self.assertRaises(ValueError) as cm:
            administracao = admin.Administracao(-12, locais.Galeria(('arte1'), '12', 'nome', ['local1']))
        excecao = cm.exception
        self.assertEqual(str(excecao), 'Não pode ter verba negativa')

    def test_deve_dar_erro_ao_nao_ter_verba_para_contratar_seguranca(self):
        administracao = admin.Administracao(13, locais.Galeria(('arte1'), '12', 'nome', ['local1']))
        self.assertEqual(administracao.contratarSeguranca(alheios.Seguranca(10)), 'É MUITO CARO')

    def test_deve_conseguir_contratar_seguranca(self):
        administracao = admin.Administracao(130000, locais.Galeria(('arte1'), '12', 'nome', ['local1']))
        seguranca = alheios.Seguranca(10)
        diminuicao = administracao.verba - seguranca.custo
        contrato = administracao.contratarSeguranca(seguranca)
        self.assertEqual(float(contrato[40:]), diminuicao)

    def test_deve_conseguir_fazer_rota(self):
        seguranca = alheios.Seguranca(10)
        data_inicio = alheios.date(2022, 12, 3)
        data_fim = alheios.date(2022, 12, 4)
        trajetoria = ['quarto1', 'quarto2']
        self.assertEqual(seguranca.rota(data_inicio, data_fim, trajetoria),
                         f"NICE! data começo:{data_inicio}, data fim: {data_fim}, {trajetoria}")

    def test_deve_adionar_local_galeria(self):
        galeria = locais.Galeria(('arte1', 'arte2'), 'endereco1', 'galeria do amigo', ['quarto1'])
        galeria.adicionaLocal(locais.Local('quarto2'))

        self.assertEqual(str(galeria.conjunto_locais[0]), 'quarto2')
