from django.conf.urls import patterns, url
from sysuser.views import SysuserDetailView
from sysuser import views

urlpatterns = patterns('',
     url(regex=r"account$",view=SysuserDetailView.as_view(),name="sysuser-detail" ),
     url(regex=r'^password/$', view='sysuser.views.password_change', name='password_change'),
     url(r'^password/done/$', 'sysuser.views.password_change_done', name='password_change_done'),
       )