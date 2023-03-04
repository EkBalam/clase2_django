from django.db import models

# Create your models here.
class Pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('Fecha de publicación')

    def __str__(self):
        return "Pregunta: " + self.texto_pregunta

class Eleccion(models.Model):
    pregunta_fk = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_eleccion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.pregunta_fk.texto_pregunta +" "+self.texto_eleccion
