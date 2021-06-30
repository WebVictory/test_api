from django.db import models

class Directory(models.Model):
    name = models.CharField(max_length=100, blank=True)
    short_name = models.CharField(max_length=100,blank=True)
    description = models.TextField (blank=True)
    version = models.CharField(max_length=100, unique=True)
    date = models.DateField()

    class Meta:
        verbose_name = 'Directory'
        verbose_name_plural = 'Directories'

    def __str__(self):
        return  self.name

class Element(models.Model):
    parent = models.ForeignKey( 'Directory' ,on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Element'
        verbose_name_plural = 'Elements'

    def __str__(self):
        return  self.value

