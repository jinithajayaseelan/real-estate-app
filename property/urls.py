from django.urls import path
from . import views

app_name= 'property'

urlpatterns = [
    path('',views.property_list, name= 'property_list'),
    path('',views.signin, name= 'signin'),
    path('',views.signup, name= 'signup'),
    path('',views.signout, name= 'signout'),
    path('<int:id>',views.property_detail, name= 'property_detail'),
]