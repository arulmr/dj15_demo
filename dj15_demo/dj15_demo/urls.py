from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dj15_demo.views.home', name='home'),
    # url(r'^dj15_demo/', include('dj15_demo.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
