from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('forweb-knust-admin-panel/', admin.site.urls),
    path('', include('pages.urls')),


    # path('tinymce/', include('tinymce.urls')),
]


admin.site.site_header = 'forWEB-KNUST'


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
