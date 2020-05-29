from django.contrib import admin
from .models import Mon
from .models import BaiHoc

# Register your models here.
class BaiHocInLine(admin.StackedInline):
    model = BaiHoc
class MonAdmin(admin.ModelAdmin):
    list_display = ['id','MaMon','TenMon']
    inlines = [BaiHocInLine]

admin.site.register(Mon, MonAdmin)
