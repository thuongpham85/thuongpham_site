from django.db import models

# Create your models here.
class NguoiDung(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    password_MaHoa = models.CharField(max_length=100, default="Chua ma hoa")

class LoaiThongBao(models.Model):
    LoaiTB = models.CharField(max_length=10)
    AnhTB = models.ImageField(blank=True, upload_to="HinhAnh/")

class ThongBao(models.Model):
    LoaiTB = models.ForeignKey(LoaiThongBao,on_delete=models.CASCADE)
    TieuDeTB = models.CharField(max_length=100)
    NoiDungTB = models.TextField()
    NgayTB = models.DateTimeField(auto_now_add=True)

class TTLienHe(models.Model):
    TenBanLH = models.CharField(max_length=20)
    TieuDeLH = models.CharField(max_length=100)
    ThongDiepLH = models.TextField()
    EmailBanLH = models.EmailField(blank=True,null=True)