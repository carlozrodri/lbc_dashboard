from django.db import models
from django.db.models.fields import FloatField, IntegerField, DecimalField
from djmoney.money import Money

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
# Create your models here.
class ValorIntroducido(models.Model):
    precio = IntegerField(default=0)
    resultado = IntegerField(default=0)
    def __str__(self):
        return str(self.precio)

class Resultados(models.Model):
    resultado = IntegerField(default=0)
    def __str__(self):
        return str(self.resultado)