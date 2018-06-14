from django.db import models

# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=False)
    descricao = models.CharField(default=None, max_length=500, blank=True)
    created = models.DateTimeField(default=None, blank=True, null=True)
    edited = models.DateTimeField(default=None, blank=True, null=True)
    removed = models.DateTimeField(default=None, blank=True, null=True)
    concluded = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        ordering=('id',)