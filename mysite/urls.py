
from django.contrib import admin
from django.urls import path, include
from website import views  # Replace 'myapp' with the name of your app
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)