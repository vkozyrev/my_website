from django.conf.urls.defaults import patterns, include, url
from django.contrib import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^applications/LuckyCookieFortune/', 'my_website.applications.views.luckyCookieFortune'),
    (r'^applications/luckycookiefortune/', 'my_website.applications.views.luckyCookieFortune'),
    #(r'^applications/', 'myproject.applications.views.listApplications'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': '/home/vkozyrev/webapps/my_website/my_website/site_media'}),
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
