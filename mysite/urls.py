
from django.contrib import admin
from django.urls import path, include
from website import views  # Replace 'myapp' with the name of your app


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.custom_login_view, name="login"),
    path('homepage/', views.homepage_view, name='homepage'),
   
]
