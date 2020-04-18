from django.urls import path
from . import views

app_name ='u_port_folio_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name= 'index'),
    path('main/',views.main,name='main'),
    path('single/',views.single,name ='single'),
    path('contact/',views.contact,name='contact-section')
]
