from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import * 


urlpatterns = [
    path('', home),
    path('contact/',contact),
    path('about/',about),
    path('blog/',blog),
    path('blog/<int:pk>', blog_single),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)