from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',  views.index, name='home'),
    path('about-us',  views.about, name='about'),
    path('Jfashion.html', views.Jfashion, name='jfashion'),
    path('Kfashion.html', views.Kfashion, name='kfashion'),
    path('minimalist.html', views.minimalist, name='minimalist'),
    path('techwear.html', views.techwear, name='techwear'),
    path('Streetwear.html', views.streetwear, name='streetwear'),
    path('gorpcore.html', views.gorpcore, name='gorpcore'),
    path('shoes.html', views.shoes, name='shoes'),
    path('shoes_str.html', views.shoes_str, name='shoes_str'),
    path('brands.html', views.brands, name='brands'),

              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
