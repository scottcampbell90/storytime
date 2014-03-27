from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    # url(r'^blog/', include('blog.urls')),
    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),

    
)
