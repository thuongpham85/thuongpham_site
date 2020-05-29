import os
from django.db import models
from AppChinh.models import NguoiDung

# Create your models here.
def taoPathchoGioiThieuMH(instance, filename):
    return os.path.join(instance.MaMon, filename)

class Mon(models.Model):
    MaMon = models.CharField(max_length=4)
    TenMon = models.TextField()
    Nam = models.IntegerField(default=1, blank=True)#blank=True tuong ung voi required=false
    HocKy = models.IntegerField(default=1, blank=True)
    GioiThieu = models.FileField(default="No file",blank=True, upload_to=taoPathchoGioiThieuMH)

def taoPathchoBH(instance, filename):
    return os.path.join(instance.mon.MaMon, filename)

class BaiHoc(models.Model):
    mon = models.ForeignKey(Mon, on_delete=models.CASCADE)
    MaBai = models.CharField(max_length=4)
    TenBai = models.TextField()
    NoiDung = models.FileField(default="No file", blank=True, upload_to=taoPathchoBH)
#    MaMon = models.CharField(max_length=4)

class BinhLuanBH(models.Model):
    baihoc = models.ForeignKey(BaiHoc, on_delete=models.CASCADE, related_name="baihocbl")
    nguoidung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    NoiDungBL = models.TextField()
    NgayBL = models.DateTimeField(auto_now_add=True)
