from django.db import models
from AppChinh.models import NguoiDung

# Create your models here.
class Mon(models.Model):
    MaMon = models.CharField(max_length=4)
    TenMon = models.TextField()
    Nam = models.IntegerField(null=True, blank=True)#blank=True tuong ung voi required=false
    HocKy = models.IntegerField(null=True, blank=True)
    GioiThieu = models.FileField(null=True, blank=True)

class BaiHoc(models.Model):
    mon = models.ForeignKey(Mon, on_delete=models.CASCADE)
    MaBai = models.CharField(max_length=4)
    TenBai = models.TextField()
    NoiDung = models.FileField(null=True, blank=True)
#    MaMon = models.CharField(max_length=4)

class BinhLuanBH(models.Model):
    baihoc = models.ForeignKey(BaiHoc, on_delete=models.CASCADE, related_name="baihocbl")
    nguoidung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    NoiDungBL = models.TextField()
    NgayBL = models.DateTimeField(auto_now_add=True)
