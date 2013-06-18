from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from enWeb.views import index

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'EnterpriseWeb.views.home', name='home'),
                       # url(r'^EnterpriseWeb/', include('EnterpriseWeb.foo.urls')),
                       url('^index/', index),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       #url(r'^admin/', include(admin.site.urls)),
)
