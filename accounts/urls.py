from django.conf.urls import url, include
from .views import *
from accounts.views import user_logout, user_login, register, user_profile
from accounts import url_reset


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^user_login/$', user_login, name='user_login'),
    url(r'^user_profile/$', user_profile, name='profile'),
    url(r'^logout/$', user_profile, name='logout'),
    url(r'^password_reset/', include(url_reset), name='password_reset'),
]