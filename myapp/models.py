from django.db import models

# Create your models here.
# Con esto lo que podemos hacer es crear clases que se convertirar en tablas de sql.


class Projects(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
