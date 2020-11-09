from api.models import Karyawan, Jabatan, Divisi
from rest_framework import serializers

class KaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karyawan
        fields = ['nama', 'alamat', 'jenis_kelamin', 'jenis_karyawan', 'no_telepon', 'email', 'no_rekening', 'pemilik_rekening', 'divisi', 'jabatan']