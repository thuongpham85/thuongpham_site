#file nay dung de dua du lieu vao base template
#luu y: phai dang ky voi setting.py tai templates_context_processors
from MonHoc.models import Mon
from .models import ThongBao

def layThongTin(request):
    dsmon = Mon.objects.all()
    tbMoiNhat = ThongBao.objects.all().order_by('-NgayTB')[:2]
    return {'dsmon': dsmon, 'tb':tbMoiNhat}