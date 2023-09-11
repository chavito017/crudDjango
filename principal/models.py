from django.db import models

# Create your models here.
class Usuarios(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=100)  

    class Meta:
        managed = True
        db_table = 'usuarios'

    def __str__(self):
        txt = "{0} ({1})"
        return txt.format(self.username, self.id)

class Temas(models.Model):
    title = models.CharField(max_length=100)  
    content = models.CharField(max_length=255)  
    fecha = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_id')

    class Meta:
        managed = True
        db_table = 'Temas'

    def __str__(self):
        return self.title

class Respuestas(models.Model):
    content = models.CharField(max_length=255)  
    creation_fecha = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_id')
    tema = models.ForeignKey('Temas', models.DO_NOTHING, db_column='Temas_id')

    class Meta:
        managed = True
        db_table = 'respuestas'

    def __str__(self):
        return self.content
