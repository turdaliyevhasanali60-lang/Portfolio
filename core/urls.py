from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from core import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)