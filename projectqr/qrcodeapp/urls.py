from django.urls import path
from qrcodeapp import views

urlpatterns = [
    path('homepage/', views.home_page),
    path('qrcreate/', views.qr_data),
    # path('test/', views.qr_dat2),

]
