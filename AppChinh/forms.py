from django import forms
import re
#from django.contrib.auth.models import User
from .models import NguoiDung,TTLienHe
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ObjectDoesNotExist

class formDangKy(forms.Form):
    #from .models import NguoiDung
    username = forms.CharField(label="Tên tài khoản", max_length=30)
    password1 = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Nhập lại mật khẩu", widget=forms.PasswordInput())

    def clean_username(self):
        ten = self.cleaned_data.get("username")
        if len(ten) < 4:
            raise forms.ValidationError("Tên tài khoản phải có ít nhất 4 ký tự!")
        if not re.search(r'^\w+$', ten):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        try:
            nd = NguoiDung.objects.get(username = ten)
        except NguoiDung.DoesNotExist:
            return ten
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def clean_password1(self):
        if "password1" in self.cleaned_data:
            mk = self.cleaned_data.get("password1")
            if len(mk) < 6:
                raise forms.ValidationError("Mật khẩu phải có ít nhất 6 ký tự!")
        return mk

    def clean_password2(self):
        if "password1" in self.cleaned_data:
            mk1 = self.cleaned_data.get("password1")
            mk2 = self.cleaned_data.get("password2")
            print (mk1,mk2)
            if mk1 != mk2:
                raise forms.ValidationError("Mật khẩu không hợp lệ!")
            else:
                return mk2
                 

    def taoNguoiDung(self):
        nd = NguoiDung()
        nd.username = self.cleaned_data.get("username")
        nd.password = self.cleaned_data.get("password1")
        nd.password_MaHoa = make_password(self.cleaned_data.get("password1"))
        nd.save()

class formDangNhap(forms.Form):
    #from .models import NguoiDung
    username = forms.CharField(max_length=30, widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        ten = self.cleaned_data.get("username")
        try:
            NguoiDung.objects.get(username = ten)
        except NguoiDung.DoesNotExist:
            raise forms.ValidationError("Tai khoan khong ton tai")
        return ten
    
    def clean_password(self):
        if "username" in self.cleaned_data:
            ten = self.cleaned_data.get("username")
            mk = self.cleaned_data.get("password")
            nd = NguoiDung.objects.get(username=ten)
            if not check_password(mk, nd.password_MaHoa):
                raise forms.ValidationError("Mat khau khong dung")
            #return nd

class formLienHe(forms.Form):
    TenBanLH = forms.CharField(max_length=20)
    TieuDeLH = forms.CharField(max_length=100)
    ThongDiepLH = forms.CharField(widget=forms.Textarea())
    EmailBanLH = forms.EmailField()

    def goiThongDiep(self):
        ten = self.cleaned_data.get("TenBanLH")
        tieude = ten + self.cleaned_data.get("TieuDeLH")
        thongdiep = self.cleaned_data.get("ThongDiepLH")
        from_email = self.cleaned_data.get("EmailBanLH")
        thongdiep = from_email + "_" + thongdiep
        if tieude and thongdiep and from_email:
            try:
                kq = send_mail(tieude, thongdiep, 'ptmthuong85@gmail.com', ['ptmthuong85@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    def taoLienHe(self):
        lh = TTLienHe()
        lh.TenBanLH = self.cleaned_data.get("TenBanLH")
        lh.TieuDeLH = self.cleaned_data.get("TieuDeLH")
        lh.ThongDiepLH = self.cleaned_data.get("ThongDiepLH")
        lh.EmailBanLH = self.cleaned_data.get("EmailBanLH")
        lh.save()

            