from django.conf.urls import url
from web import views

app_name = 'web'
urlpatterns = [
    url(r'^$', views.find_bus, name='home'), 
    url(r'^profile/', views.user_profile, name='profile'),
    url(r'^select/', views.select, name='select'),
]