from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.http import HttpResponseRedirect, Http404
from AppChinh.models import NguoiDung

# Create your views here.

def menu_MonHoc(request):
    from .models import Mon
    Data = {'DSMon': Mon.objects.all()}
    return render(request, 'Mon/menuMon.html', Data)

def showThongTinMH(request, id):
    from .models import Mon, BaiHoc
    #queryset = BaiHoc.objects.filter(mon__MaMon=mavao) #cú pháp <tên khóa ngoại>__<tên thuộc tính của bảng khác>=<giá trị>
    try:
        mh = Mon.objects.get(id=id)
    except Mon.DoesNotExist:
        raise Http404("Môn học này không tồn tại!")
    
    queryset = BaiHoc.objects.select_related('mon').filter(mon_id=id)
    bhs = [] 
    for bh in queryset:
        bhs.append({'id':bh.id, 'MaBai': bh.MaBai, 'TenBai': bh.TenBai, 'MaMon': mh.MaMon})
    return render(request, 'Mon/ThongTinMH.html', {'bhs': bhs,'mh': mh})

def showGioiThieuMH(request, id):
    from .models import Mon
    try:
        mh = Mon.objects.get(id=id)
    except Mon.DoesNotExist:
        raise Http404("Môn học này không tồn tại!")
    return render(request, 'Mon/GioiThieuMH.html', {'mh': mh})

def showBaiHoc(request, idmon, id):
    from .models import BaiHoc
    from .forms import formBinhLuan
    try:
        bh = BaiHoc.objects.get(mon_id=idmon,id=id)
    except BaiHoc.DoesNotExist:
        raise Http404("Bài học này không tồn tại!")
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


