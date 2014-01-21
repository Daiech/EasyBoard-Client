from django.conf.urls import patterns, url

urlpatterns = patterns('apps.app4.views',
    url(r'^ajax/$', "home", name="home_app4"),
)