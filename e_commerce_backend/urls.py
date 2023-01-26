from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from store.urls import urlpatterns as storePatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    path('',include('order.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns +=storePatterns