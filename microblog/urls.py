from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
#from blog.views import blog_list, blog_detail
from . import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^microblog/', include('microblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^$', views.HomepageView.as_view(), name="home"),
    url(r'^blog/', include("blog.urls", namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
)
