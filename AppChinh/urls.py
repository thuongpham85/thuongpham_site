from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('lienhe/', views.contact),
    path('dangky/', views.dangKy, name='Dangky'),
    path('dangnhap/', views.dangNhap, name='Dangnhap'),
    #path('dangnhap/',auth_views.LoginView.as_view(template_name = "pages/DangNhap.html"), name='Dangnhap'),
    path('logout/', auth_views.LogoutView.as_view(next_page ="/"), name = "Logout"),
    path('ThongBao/', views.ThongBaoListView.as_view(), name="tbao"),
    path('ThongBao/<int:pk>/', views.ThongBaoDetailView.as_view(), name="tbct"),#Vi DetailView truy van bang primary key cua model nen ta dua vao bien pk, int:pk the hien bien pk voi kieu du lieu la int
]