from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^register_handle/', views.register_handle, name='register_handle'),
    url(r'^login/', views.login, name='login'),
    url(r'^loginhandle/',views.loginhandle,name='loginhandle')
]
