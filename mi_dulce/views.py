from django.shortcuts import render, redirect
from django.db.models import Q

from .models import *

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template

# Create your views here.
def index(request):
	categorias=Categoria.objects.all()
	producto_destacados=Producto.objects.filter(destacado=True)
	alerta=''
	if request.GET:
		alerta= request.GET['a']

	dic={'categorias':categorias,'destacados':producto_destacados,'alerta':alerta}

	return render(request,'mi_dulce/index.html',dic)

def sobre_nosotros(request):
	categorias=Categoria.objects.all()
	dic={'categorias':categorias}
	return render(request,'mi_dulce/sobre_nosotros.html',dic)

def productos(request):
	categorias=Categoria.objects.all()
	if request.GET:
		idcat=request.GET['id']
		categoria=Categoria.objects.get(idcategoria=idcat)
		productos= Producto.objects.filter(Q(categoria_1=categoria)|Q(categoria_2=categoria))
	else:
		productos= Producto.objects.all()
	dic={'categorias':categorias,'productos':productos}

	return render(request,'mi_dulce/productos.html',dic)

def item(request):
	categorias=Categoria.objects.all()
	if request.GET:
		idpro=request.GET['id']
		producto= Producto.objects.get(idproducto=idpro)
		categoria= producto.categoria_1
		relacionados= Producto.objects.filter(Q(categoria_1=categoria)|Q(categoria_2=categoria)).order_by('?')[:4]
	else:
		return redirect('/')

	dic={'categorias':categorias,'producto':producto,'relacionados':relacionados}
	return render(request,'mi_dulce/item.html',dic)

def contacto(request):
	if request.POST:
		tel = request.POST['phone']
		email = request.POST['email']
		nombre = request.POST['name']
		asunto = request.POST['Title']
		mensaje = request.POST['message']

		template = get_template('mi_dulce/email_contacto.html')

		context = {'nombre': nombre, 'telefono': tel, 'email': email, 'mensaje': mensaje, 'asunto': asunto}
		contenido = template.render(context)
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['anaflavia_albareda@hotmail.com',]
		asunto='Contacto a través de la Web Dulceideas'
		send_mail( asunto, contenido, email_from, recipient_list,fail_silently = False)
		url = '/?a=Mensaje%20Enviado#extForm17-i'

	return redirect(url)
