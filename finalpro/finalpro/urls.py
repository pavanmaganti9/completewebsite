from django.conf.urls import include, url
from django.contrib import admin
#from django_filters.views import FilterView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'finalpro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', include('website.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^website/', include('website.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)