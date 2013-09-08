from django.conf.urls import patterns, url
from sysuser.views import SysuserDetailView
from sysuser import views

urlpatterns = patterns('',
     url(regex=r"account$",view=SysuserDetailView.as_view(),name="sysuser-detail" ),)