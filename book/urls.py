from django.conf.urls import url
from book import views

app_name = 'book'
urlpatterns = [
    url(r'^book/', views.book_bus, name='booking'),   
    url(r'^payment/', views.payment, name='payment'),  
    url(r'^seats/(?P<bus_number>\w+)$', views.book_seats, name='seats'),
    url(r'^success/', views.final, name='success'),
]