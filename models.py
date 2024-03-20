from django.db import models

class Url(models.Model):
    url=models.CharField(max_length=100)
    class Meta:
        db_table = "urls"

class Url_new(models.Model):
    terminos_busqueda=models.CharField(max_length=500)
    industria=models.CharField(max_length=100)
    email=models.EmailField()
    class Meta:
        db_table = "url_new"
        
