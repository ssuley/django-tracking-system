from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^driver/$', views.reg_Driver)
]