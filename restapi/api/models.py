from __future__ import unicode_literals
from django.db import models

class Divisi (models.Model):
    nama = models.CharField(max_length=100)
    keterangan =models.TextField(blank=True)

    def __str__(self):
        return self.nama

class Jabatan (models.Model):
    nama = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return self.nama

class Karyawan (models.Model):
    JENIS_KELAMIN_CHOICES = (
        ('pria', 'Pria'),
        ('wanita', 'Wanita'),
    )

    JENIS_KARYAWAN_CHOICES = (
        ('magang', 'Magang'),
        ('kontrak', 'Kontrak'),
        ('tetap', 'Tetap'),
    )

    nama = models.CharField(max_length=100)
    alamat = models.TextField(blank=True)
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN_CHOICES)
    jenis_karyawan = models.CharField(max_length=10, choices=JENIS_KARYAWAN_CHOICES)
    no_telepon = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100, blank=True)
    no_rekening = models.CharField(max_length=100)
    pemilik_rekening = models.CharField(max_length=100)
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama