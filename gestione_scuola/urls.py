from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'sysuser.views.password_change'),
    url(r'^login/$', 'gestione_scuola.views.login_user', name='login'),
    url(r'^logout/$', 'gestione_scuola.views.logout', name='logout'),
    url(r'^user/',include('sysuser.urls')),
    url(r'^account/',include('account.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
