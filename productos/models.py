from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Las imágenes se subirán a la carpeta 'productos/' dentro de 'media'
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre