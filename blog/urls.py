from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index_page, name='index_page'),
    url(r'^about/$', views.about_page, name='about_page'),
    url(r'^research/$', views.research_page, name='research_page'),
    url(r'^member/$', views.member_page, name='member_page'),
    url(r'^notice/$', views.notice_page, name='notice_page'),
    url(r'^contact/$', views.contact_page, name='contact_page'),

]
