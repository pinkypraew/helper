from django.conf.urls import patterns, url
#from django.contrib import admin
from rango import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

                       #url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.index, name='index'),
                       #url(r'^rango/', include(rango.urls)),
# url(r'index/$',index),
)
