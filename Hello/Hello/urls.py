"""Hello URL Configuration

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
from django.contrib import admin
from django.urls import path, include


# Below code is to change the default text for Admin panel.
admin.site.site_header  =  "Test admin"  
admin.site.site_title  =  "Test admin site"
admin.site.index_title  =  "Test Admin"

urlpatterns = [
    path('admin/', admin.site.urls),

    # Below path will take the control to the home app.
    path('', include('home.urls')) 
]
