from django.contrib import admin
from .models import Task, ValorIntroducido, Resultados

# Register your models here.
admin.site.register(Task)
admin.site.register(ValorIntroducido)
admin.site.register(Resultados)
