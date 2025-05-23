from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=90)

    def __str__(self):
        return f"{self.nome} ({self.id})"


class Meta:
    verbose_name = "Autor"
    