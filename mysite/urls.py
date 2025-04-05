
from django.contrib import admin
from django.urls import path, include
from website import views  
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.custom_login_view, name="login"),
    path('application/', views.application, name="application"),
    path('logout/', views.logout_view, name='logout'),
    path('<str:page>/', views.page_detail, name='page_detail'),

   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)