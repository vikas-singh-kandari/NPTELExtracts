from django.urls import path, include
from api import views
from django.conf import settings
from django.conf.urls.static import static
from api.views import download_excel, CertificateViewSet, login_view,signup_view, logout_view
from django.contrib import admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'certificates', CertificateViewSet)

urlpatterns = [
    path('father/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.upload_certificates, name='upload_certificates'),
    path('download-excel/', download_excel, name='download_excel'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 