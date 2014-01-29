from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'launcher.views.launcher', name='client_home'),
    url(r'', include('EasyBoard.urls')),
    
    url(r'^carnetizacion/', include('EasyBoard.extra_apps.school_card.urls')),
    url(r'^app4/', include('apps.app4.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
