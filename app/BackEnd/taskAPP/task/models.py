from django.db import models

# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=False)
    descricao = models.CharField(default=None, max_length=500, blank=True)
    created = models.DateField(default=None, blank=True)
    edited = models.DateField(default=None, blank=True)
    removed = models.DateField(default=None, blank=True)
    concluded = models.DateField(default=None, blank=True)

    class Meta:
        ordering=('created',)