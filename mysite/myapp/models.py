from django.db import models
  
class Estilo(models.Model):
 nombre = models.CharField(max_length=30)
 
 def __str__(self):
  return self.nombre
 
class Interprete(models.Model):
 nombre = models.CharField(max_length=30)
 DNI = models.CharField(max_length=9)
 fecha = models.DateField()
 descripcion = models.TextField(max_length=1000)
 pass
 
 def __str__(self):
  return self.nombre
  
class Cancion(models.Model):
 titulo = models.CharField(max_length=30)
 interprete = models.ManyToManyField(Interprete)
 fecha = models.DateField()
 estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)
 popularidad = models.IntegerField()
 popularidad_estilo = models.IntegerField()
 link = models.CharField(max_length=300)
 
 def __str__(self):
  return self.titulo
