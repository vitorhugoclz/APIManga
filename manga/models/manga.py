from django.db import models

class Manga(models.Model):
    """
    Uma classe que representa um Manga

    Attributes
    ----------
    titulo : models.CharField, max_length=350
        titulo do Manga
    data_lancamento : models.DateField
        Data em que o Manga foi lançado
    """

    titulo : models.CharField = models.CharField(max_length=350)
    data_lancamento : models.DateField = models.DateField()

    class Meta:
        """
        Para modelos divididos em arquivos separados, especifique o nome da tabela e o nome do aplicativo.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "manga"
        app_label = "manga"