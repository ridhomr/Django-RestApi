from rest_framework import viewsets
from api.serializers import KaryawanSerializer
from api.models import Karyawan, Jabatan, Divisi
from rest_framework.response import Response

class KaryawanViewSet(viewsets.ModelViewSet):
    queryset =  Karyawan.objects.all()
    serializer_class = KaryawanSerializer