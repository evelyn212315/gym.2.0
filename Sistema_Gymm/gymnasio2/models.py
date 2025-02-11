from django.db import models

class Producto(models.Model):
    codigo_prod = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    
class Meta:
      verbose_name = 'Producto'
      verbose_name_plural = 'productos'
      db_table = 'producto'

def str(self):
    return self.nombre
      

class Cliente(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def str(self):
        return self.cedula

class Meta:
    verbose_name = 'cliente'
    verbose_name_plural = 'clientes'
    db_table = 'cliente'
def _str_(self):
      return self.cedula

class Instructor(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
     
class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = ' instructores'
        db_table = 'instructor'

def str(self):
      return self.nombre