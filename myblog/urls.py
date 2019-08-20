"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainsite.views import homepage,showpost
from mysite.views import about, listing,disp_detail, index1
from mymodel import views

urlpatterns = [

    url(r'^$', homepage),
    url(r'^m$', views.index),
    url(r'^detail/(\d+)$',views.detail,name='detail-url'),
    url(r'^post/(\w+)$', showpost),
    url(r'^admin/', admin.site.urls),
    url(r'^about/', about),
    url(r'^list/([0-9a-zA-Z]+)/$', disp_detail),
    url(r'^list/', listing),
    url(r'^1$', index1),
]
