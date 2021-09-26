from django.contrib import admin
from django.urls import path
from product import views
urlpatterns = [
    path("",views.index,name='home'),
    path("tshirt",views.tshirt,name='tshirt'),    
    path("access",views.access,name='access'),   
    path("anime",views.anime,name='anime'),   
    path("cart",views.cart,name='cart'),   
    path("music",views.music,name='music'),   
    path("sl",views.sl,name='sl'),   
    path("funky",views.funky,name='funky'),   
    path("stshirt",views.stshirt,name='stshirt'),   
    path("trending",views.trending,name='trending'),   
    path("sup",views.sup,name='sup'),   
    path("discount",views.discount,name='discount'),   
]

