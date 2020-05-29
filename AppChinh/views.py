from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from MonHoc.models import Mon
from .models import ThongBao, LoaiThongBao
from django.views.generic import ListView, DetailView
#from django.template import RequestContext

# Create your views here.
def index(request):
    Data = ThongBao.objects.all().order_by('-NgayTB')[:1]
    return render(request, "pages/TrangChu.html", {'TB':Data})

def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})
    
def contact(request):
    from .forms import formLienHe
    formlh = formLienHe()
    if request.method == "POST":
        formlh = formLienHe(request.POST)
        if formlh.is_valid():
            formlh.goiThongDiep()
            formlh.taoLienHe()
            return HttpResponseRedirect("/")
    return render(request, "pages/Lienhe.html", {'form': formlh})

def dangKy(request):
    from .forms import formDangKy
    form = formDangKy()
    if request.method == 'POST':
        form = formDangKy(request.POST)
        if form.is_valid():
            form.taoNguoiDung()
            return HttpResponseRedirect('/')
    return render(request, 'pages/DangKy.html', {'form': form})

def dangNhap(request):
    from .forms import formDangNhap
    formdn = formDangNhap()
    if request.method == 'POST':
        formdn = formDangNhap(request.POST)
        if formdn.is_valid():
            username = formdn.cleaned_data['username']
            request.session['username'] = username #them username vao session de su dung cho phien lam viec khi login thanh cong
            return HttpResponseRedirect('/')
            #return render(request, 'pages/TrangChu.html', {'username': username})
    return render(request, 'pages/DangNhap.html', {'form': formdn})

class ThongBaoListView(ListView):
    queryset = ThongBao.objects.all().order_by('-NgayTB')
    template_name = 'pages/ThongBao.html'
    context_object_name='tbs'
    paginate_by=5

#Lop ThongBaoDetailView ke thua lop DetailView. Vi DetailView se truy van bang primarykey nen ta dua pk vao
#khai bao model de biet se truy van tai dau
class ThongBaoDetailView(DetailView):
    model = ThongBao
    template_name='pages/ThongBaoChiTiet.html'
