from datetime import date
from django.test import TestCase
from manga.models.manga import Manga

class TestManga(TestCase):
    """
    Executa os tests relacionado ao modelo Manga

    Methods
    -------
    setUp()
        instancia os valores necessários para os testes
    test_atributos_manga()
        verifica se uma instancia da classe Manga está com os valores esperados    
    """

    def setUp(self) -> None:
        """
        Prepara setup para os test da classe
        """
        self.manga:Manga = Manga(titulo='Manga Generico', data_lancamento=date.today())


    def test_atributos_manga(self):
        """Verifica atributos de uma instancia de manga não armazenada no banco de dados"""
        self.assertEqual(self.manga.titulo, 'Manga Generico')
        self.assertEqual(self.manga.data_lancamento, date.today())
