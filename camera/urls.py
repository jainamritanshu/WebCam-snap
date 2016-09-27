from django.conf.urls import patterns, include, url
from django.contrib import admin
from cam import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'camera.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/$', views.list_cam, name = 'list_cam'),
    url(r'^downloading/$', views.cam_click, name = 'cam_click'),
)
