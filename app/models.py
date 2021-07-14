from django.db import models
# Create your models here.
class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='autos', max_length=255, blank=False, null=False, default='-')
    marca = models.CharField(max_length=100, blank=False, null=False)
    modelo = models.CharField(max_length=100, blank=False, null=False)
    precio = models.IntegerField(verbose_name='Precio', null=True)
    año = models.IntegerField(verbose_name='Año del Modelo', null=True)
    combustible = models.CharField(max_length=50, blank=False, null=False)
    color = models.CharField(max_length=50, blank=False, null=False)
    tipo_vehiculo = models.CharField(max_length=50, blank=False, null=False)
    tipo_caja = models.CharField(max_length=50, blank=False,null=False)
    aire_acondicionado= models.CharField(max_length=50, blank=False, null=False)
    alzavidrios = models.CharField(max_length=50, blank=False, null=False)
    direccion_hidraulica=models.CharField(max_length=50, blank=False, null=False)
    tranmision_auto = models.CharField(max_length=50)
    espejos= models.CharField(max_length=50)
    radio=models.CharField(max_length=50)
    
    def __str__(self):
        return f'ID: {self.id}, Marca: {self.marca}'

    class Meta:
        db_table = 'autos'
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'
        ordering = ['id']
