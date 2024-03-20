from django.urls import path
from add_URL import views
urlpatterns = [
    path('', views.home, name="home"),
    path('url_new', views.url_new, name="url_new"),
    path('blog', views.blog, name="blog"),
    path('contacto', views.contacto, name="contacto"),
    path('compra', views.compra, name="compra"),
    path('base', views.base, name="base"),

]