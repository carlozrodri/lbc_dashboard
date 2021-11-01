from django.db import models
from django.db.models.fields import FloatField, IntegerField, DecimalField


# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
# Create your models here.
class ValorIntroducido(models.Model):
    precio = FloatField(default=0)
    resultado = IntegerField(default=0)
    def __str__(self):
        return str(self.precio)

class Resultados(models.Model):
    resultado = FloatField(default=0)
    def __str__(self):
        return str(self.resultado)

class Paises(models.Model):
    country = (
        ('ves', 'Venezuela'),
        ('usd', 'United states'),
        ('gbp', 'United kingdom'),
    )
    pais = models.CharField(max_length=3, choices=country, primary_key=True)

    def __str__(self):
        return self.name
