from django.urls import path
from . import views

urlpatterns=[
	path('', views.index, name='index'),
	path('sobre_nosotros/',views.sobre_nosotros, name='sobre_nosotros'),
	path('productos/',views.productos,name='productos'),
	path('item/',views.item,name='item'),
	path('contacto/',views.contacto,name='contacto'),
]