from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'street_safe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'$^', 'heatmap.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', 'heatmap.views.about', name='about'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
