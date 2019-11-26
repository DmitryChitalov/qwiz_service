"""qwizsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

import mainapp.views as mainapp

urlpatterns = [
    # path('admin/', admin.site.urls),

    re_path('^$', mainapp.index, name='index'),
    re_path('^games/$', mainapp.games, name='games'),
    re_path('^galery/$', mainapp.galery, name='item'),
    re_path('^leadboard/$', mainapp.leadboard, name='leadboard'),
    re_path('^victorina/$', mainapp.victorina, name='victorina'),
    re_path('^victorina/qwestions/(?P<pk>\d+)/$', mainapp.qwestions, name='qwestion'),
    re_path('^reg/$', mainapp.registration, name='reg'),
    re_path('^reg/success/$', mainapp.success, name='success'),


    re_path('^admins/', include('adminapp.urls', namespace='admins')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
