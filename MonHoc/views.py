from django.shortcuts import render
from .models import Mon, BaiHoc
from django.http import HttpResponse, FileResponse
#from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponseRedirect
from .forms import formBinhLuan
from AppChinh.models import NguoiDung

# Create your views here.

def menu_MonHoc(request):
    Data = {'DSMon': Mon.objects.all()}
    return render(request, 'Mon/menuMon.html', Data)

def showThongTinMH(request, id):
    #queryset = BaiHoc.objects.filter(mon__MaMon=mavao) #cú pháp <tên khóa ngoại>__<tên thuộc tính của bảng khác>=<giá trị>
    queryset = BaiHoc.objects.select_related('mon').filter(mon_id=id)
    bhs = []
    mh = Mon.objects.get(id=id)
    for bh in queryset:
        bhs.append({'id':bh.id, 'MaBai': bh.MaBai, 'TenBai': bh.TenBai, 'MaMon': mh.MaMon})
    return render(request, 'Mon/ThongTinMH.html', {'bhs': bhs,'mh': mh})

def showGioiThieuMH(request, id):
    mh = Mon.objects.get(id=id)
    return render(request, 'Mon/GioiThieuMH.html', {'mh': mh})

def showBaiHoc(request, idmon, id):
    bh = BaiHoc.objects.get(mon_id=idmon,id=id)
    if request.session.get("username"):
        nd = NguoiDung.objects.get(username=request.session.get("username"))
    form = formBinhLuan()
    if request.method == "POST":
        form = formBinhLuan(request.POST, baihoc = bh, nguoidung=nd)
        if form.is_valid():
            form.save()
            print (nd.username)
            return HttpResponseRedirect(request.path)
    return render(request, 'Mon/BaiHoc.html', {'bh': bh, 'form':form})


