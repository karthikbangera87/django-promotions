from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myapp.views.home', name='home'),
    url(r'^(?P<reference_id>.*)$', 'myapp.views.share', name='share'),
    # url(r'^blog/', include('blog.urls')),

    
)
