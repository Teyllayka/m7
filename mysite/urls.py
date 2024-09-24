
from django.contrib import admin
from django.urls import path, include
from website import views  # Replace 'myapp' with the name of your app
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.custom_login_view, name="login"),
    path('homepage/', views.homepage_view, name='homepage'),
    path('pvr/', views.pvr, name="pvr"),
    path('ppb/', views.ppb, name="ppb"),
    path('application/', views.application, name="application"),
    path('kpp/', views.kpp, name="kpp"),
    path('kalendar/', views.calendar, name="calendar"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

   
]
