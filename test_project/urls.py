"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path, include
#from django.conf import settings #
#from django.conf.urls.static import static#
#DataFlair #Static-files Tutorial
#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('hello_world.urls'))
    #path('registration/', include('registration')),
    #path('', include('home.urls')),

#]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#
from django.contrib import admin  
from django.urls import path  
from note import views
#from register import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('register/', include('register.urls', namespace='register')),
    #path('note/', include('note.urls', namespace='note')),
    #path('', views.home),
    #path('create', views.create),
    #path('login', views.login), 
    path('no', views.no),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]


