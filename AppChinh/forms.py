from django import forms
import re
#from django.contrib.auth.models import User
from .models import NguoiDung
from django.contrib.auth.hashers import make_password

class formDangKy(forms.Form):
    
    username = forms.CharField(label="Tên tài khoản", max_length=30)
    password1 = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Nhập lại mật khẩu", widget=forms.PasswordInput())

    def clean_password2(self):
        if "password1" in self.cleaned_data:
            mk1 = self.cleaned_data.get("password1")
            mk2 = self.cleaned_data.get("password2")
            if mk1 == mk2 and mk1:
                return mk2
        raise forms.ValidationError("Mật khẩu không hợp lệ!")

    def clean_username(self):
        ten = self.cleaned_data.get("username")
        if not re.search(r'^\w+$', ten):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        try:
            NguoiDung.objects.get(username = ten)
        except NguoiDung.DoesNotExist:
            return ten
        raise forms.ValidationError("Tài khoản không tồn tại")

    def taoNguoiDung(self):
        nd = NguoiDung()
        nd.username = self.cleaned_data.get("username")
        nd.password = self.cleaned_data.get("password1")
        nd.save()

class formDangNhap(forms.Form):
    
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nhap username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Nhap mat khau'}))

    def clean_username(self):
        ten = self.cleaned_data.get("username")
        try:
            NguoiDung.objects.get(username=ten)
        except NguoiDung.DoesNotExist:
            raise forms.ValidationError("Tai khoan khong ton tai")
        return ten
    
    def clean_password(self):
        ten = self.cleaned_data.get("username")
        mk = self.cleaned_data.get("password")
        nd = NguoiDung.objects.get(username=ten)
        if mk != nd.password:
            raise forms.ValidationError("Mat khau khong dung")
        return nd

#    def hienThi(self):
#        ten = self.cleaned_data.get("username")
#        mk = self.cleaned_data.get("password")
#        nd = NguoiDung.objects.get(username=ten, password=mk)
#        return nd
    

            