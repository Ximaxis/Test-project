"""ladamedia_test URL Configuration

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
from django.urls import path
from django.urls import re_path
import mainapp.views as mainapp


urlpatterns = [
    path("admin", admin.site.urls),
    re_path(r"^$", mainapp.main, name='main'),
    re_path(r"^select/$", mainapp.select, name='select'),

    re_path(r"^order_header/create/$", mainapp.OrderHeadersCreateView.as_view(),
            name="order_header_create"),
    re_path(r"^order_header/read/$", mainapp.order_header, name="order_header"),
    re_path(r"^order_header/update/(?P<pk>\d+)/$", mainapp.OrderHeadersUpdateView.as_view(),
            name="order_header_update"),
    re_path(r"^order_header/delete/(?P<pk>\d+)/$", mainapp.OrderHeadersDeleteView.as_view(),

            name="order_header_delete"),
    re_path(r"^order_header/(?P<pk>\d+)/order_details/create/$", mainapp.OrderDetailsCreateView.as_view(),
            name="order_details_create"),
    re_path(r"^order_header/(?P<pk>\d+)/order_details/read/$", mainapp.order_details,
            name="order_details"),
    re_path(r"^order_header/(?P<pk>\d+)/order_details/delete/$", mainapp.order_details_delete,
            name="order_details_delete"),
    re_path(r"^order_header/(?P<pk>\d+)/order_details/update/$", mainapp.order_details_update,
            name="order_details_update"),
]
