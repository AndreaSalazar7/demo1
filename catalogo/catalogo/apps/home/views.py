from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render_to_response
from django.template import RequestContext
from catalogo.apps.ventas.models import *
from catalogo.apps.home.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage #paginacion

def contact_view (request):
	formulario = contact_form()
	ctx = {'form':formulario}
	return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request) )

def about_view (request):
	return render_to_response('home/about.html', context_instance = RequestContext(request))

def index_view (request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))
def contact_view (request):
	info_enviado = False 
	email = ""
	title = ""
	text = ""
	if request.method == "POST":
		formulario = contact_form(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['correo']
			title = formulario.cleaned_data['titulo']
			text = formulario.cleaned_data['texto']
	else:
		formulario = contact_form()
	ctx = {'form':formulario,'email':email,"title":title, "text":text,"info_enviado":info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))

def single_product_view(request, id_prod):
	prod = Producto.objects.get(id = id_prod) 
	ctx = {'producto':prod}
	return render_to_response('home/single_producto.html',ctx,context_instance = RequestContext(request))

def single_marca_view(request, id_prod):
	prod = Marca.objects.get(id = id_prod) 
	ctx = {'marca':prod}
	return render_to_response('home/single_marca.html',ctx,context_instance = RequestContext(request))

def single_categoria_view(request, id_prod):
	prod = Categoria.objects.get(id = id_prod) 
	ctx = {'categoria':prod}
	return render_to_response('home/single_categoria.html',ctx,context_instance = RequestContext(request))

def productos_view(request, pagina):
	lista_prod = Producto.objects.filter(status=True)
	#lista_prod = Producto.objects.all().count() 
	paginator = Paginator(lista_prod, 5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)

	ctx = {'productos' :productos}
	return render_to_response ('home/productos.html', ctx, context_instance = RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated(): #verificamos si el usuario ya esta authenticado o logueado
		return HttpResponseRedirect('/') #si esta logueado lo redirigimos a la pagina pricipal
	else: #si no esta authenticado
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o clave incorrecta"
	formulario = Login_form()
	ctx = {'form':formulario, 'mensaje':mensaje}
	return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/') 

def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save() # Guardar el objeto
			return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
