from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_MonHoc),
    path("<id>/", views.showThongTinMH ),
    path("<id>/GioiThieuMH.html", views.showGioiThieuMH),
    path("<idmon>/Bai_<id>/", views.showBaiHoc, name="baihoc"),
]