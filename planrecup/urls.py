from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from content.views.content import ContentView
from content.views.front import FrontView

handler404 = 'content.views.front.handler404'
handler500 = 'content.views.front.handler500'

admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^medias/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    
    url(r'^$',
        FrontView.as_view(),
        name='home',
        kwargs={'action': FrontView.default_action}),
    
    url(r'^$',
        FrontView.as_view(),
        name=FrontView.view_name),
    
    url(FrontView.get_url_regexp(),
        FrontView.as_view(),
        name=FrontView.view_name),
    
    url(r'^dashboard/', include('content.dashboard.urls')),
    url(r'^dashboard/digger/', include('content.digger.urls')),
    url(r'^dashboard/todo/', include('content.todo.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(ContentView.get_url_regexp('.*?'),
        ContentView.as_view(),
        name=ContentView.view_name),
)
