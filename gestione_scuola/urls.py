from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^main/$', 'gestione_scuola.views.main'),
    url(r'^login/$', 'gestione_scuola.views.login_user', name='login'),
    # url(r'^gestione_scuola/', include('gestione_scuola.foo.urls')),

    url(r'^user/',include('sysuser.urls')),
    url(r'^account/',include('account.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
