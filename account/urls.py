from django.conf.urls import patterns, url
from account.views import PasswordChangeView


# place app url patterns here
urlpatterns = patterns('',
     url(regex=r"passwd$",view=PasswordChangeView.as_view(),name="password" ),)