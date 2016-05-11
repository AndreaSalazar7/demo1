from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('catalogo.apps.home.views',
		url(r'^index/$','index_view', name = 'vista_principal'),
		url(r'^$', 'about_view', name = 'vista_about'),
		url(r'^contacto/$','contact_view', name = 'vista_contacto'),
		url(r'^producto/(?P<id_prod>.*)/$', 'single_product_view', name = 'vista_single_producto'),
		url(r'^marca/(?P<id_prod>.*)/$', 'single_marca_view', name = 'vista_single_marca'),
		url(r'^categoria/(?P<id_prod>.*)/$', 'single_categoria_view', name = 'vista_single_categoria'),
		url(r'^productos/$', 'productos_view', name = 'vista_productos'),
		url(r'^registro/$','register_view',name='vista_registro'),
		url(r'^productos/page/(?P<pagina>.*)/$', 'productos_view', name = 'vista_productos'),
		
		url(r'^login/$', 'login_view', name = 'vista_login'),
		url(r'^logout/$', 'logout_view', name = 'vista_logout'),
)