from django.urls import path
from . import views

urlpatterns=[
    path('masterpage',views.linking_masterpage,name='masterpage'),
    path('home',views.linking_home,name='home'),
    path('about',views.linking_about,name='about'),
    path('contact',views.linking_contact,name='contact')

]