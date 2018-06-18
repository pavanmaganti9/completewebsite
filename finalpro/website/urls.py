from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^backend/', views.backend, name='backend'),
	url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^login/$', views.login, name='login'),
	url(r'^form/$', views.form, name='form'),
	url(r'^formsubmit/$', views.formsubmit, name='formsubmit'),
	url(r'^submitted_data/$', views.submitted_data, name='submitted_data'),
	url(r'^formdetails/(?P<id>\d+)/$', views.formdetails, name='formdetails'),
	#url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
	url(r'^search/$', views.search, name='search'),
	url(r'^fileupload/$', views.fileupload, name='fileupload'),
	
]
