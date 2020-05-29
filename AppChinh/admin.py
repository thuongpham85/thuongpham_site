from django.contrib import admin
from .models import NguoiDung, LoaiThongBao, ThongBao

# Register your models here.
class NguoiDungAdmin(admin.ModelAdmin):
    list_display = ['username','password', 'password_MaHoa']

class LoaiTBAdmin(admin.ModelAdmin):
    list_display=['LoaiTB','AnhTB']

class ThongBaoAdmin(admin.ModelAdmin):
    list_display=['TieuDeTB', 'NoiDungTB','NgayTB','LoaiTB']

admin.site.register(NguoiDung, NguoiDungAdmin)
admin.site.register(LoaiThongBao, LoaiTBAdmin)
admin.site.register(ThongBao,ThongBaoAdmin)