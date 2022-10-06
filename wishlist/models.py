from django.contrib.auth.models import User
from django.db import models
from django import forms

# Create your models here.
class BarangWishlist(models.Model):
    user = models.ForeignKey(
                User,
                models.SET_NULL,
                blank=True,
                null=True
            )
    nama_barang = models.CharField(max_length=50)
    harga_barang = models.IntegerField()
    deskripsi = models.TextField()

class AddWishlistForm(forms.ModelForm):
    class Meta:
        model = BarangWishlist
        fields = ('nama_barang', 'harga_barang', 'deskripsi')
        widgets = {
            'deskripsi': forms.Textarea(),
        }