from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    #Lab 1
    path('', show_wishlist, name='show_wishlist'),
    #Lab 2
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    #Lab 3
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]