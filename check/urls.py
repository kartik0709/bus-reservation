from django.conf.urls import url
from check import views

app_name = 'check'
urlpatterns = [
    url(r'^checkreservation/', views.check_reservation, name='check_reservation'),    
    url(r'^showticket/', views.show_ticket, name='show_ticket'),  
]