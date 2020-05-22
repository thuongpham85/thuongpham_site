from django import forms
from .models import BinhLuanBH

class formBinhLuan(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.baihoc = kwargs.pop('baihoc', None)
        self.nguoidung = kwargs.pop('nguoidung', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        binhluan = super().save(commit=False)
        binhluan.baihoc = self.baihoc
        binhluan.nguoidung = self.nguoidung
        binhluan.save()

    class Meta:
        model = BinhLuanBH
        fields = ["NoiDungBL"]
        #widgets = {
         #   "NoiDungBL": forms.Textarea(attrs={'width':'200px', 'height':'80px'})
        #}