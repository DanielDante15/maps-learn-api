from django.db import models


class Empresas(models.Model):
    razao_social = models.CharField(max_length=50)
    
