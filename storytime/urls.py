from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'story.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact/', 'storytime.views.contact', name='contact'),
    (r'^articles/', include('article.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)
