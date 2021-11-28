from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100 , verbose_name = 'Category Name' )
    #verbose_name yazarak admin panelini override ederek nasil gözükmesini istiyorsak onu gösterebiliriz.
    def __str__(self):
        return self.name

