from django.db import models

# Create your models here.
class NguoiDung(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

class LoaiThongBao(models.Model):
    LoaiTB = models.CharField(max_length=10)
    AnhTB = models.ImageField(blank=True)
class ThongBao(models.Model):
    LoaiTB = models.ForeignKey(LoaiThongBao,on_delete=models.CASCADE)
    TieuDeTB = models.CharField(max_length=100)
    NoiDungTB = models.TextField()
    NgayTB = models.DateTimeField(auto_now_add=True)