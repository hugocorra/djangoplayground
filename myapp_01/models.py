from django.db import models
from django.urls import reverse


class A(models.Model):
    field_ma = models.CharField(max_length=100, verbose_name='A_Field')

    def get_absolute_url(self):
        return reverse('myapp_01:detail', args=[str(self.id)])


class B(models.Model):
    fk = models.ForeignKey(A, on_delete=models.CASCADE)
    field_mb = models.CharField(max_length=100, verbose_name='B_Field')


class C(models.Model):
    fk = models.ForeignKey(A, on_delete=models.CASCADE)
    field_mc = models.CharField(max_length=100, verbose_name='C_Field')
