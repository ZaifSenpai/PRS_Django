"""PRS URL Configuration

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
from django.conf.urls import url, include
from api.resources import SmsResource
from api.resources import RecommendationResource
from api import views
from django.views.generic import RedirectView

sms_resource = SmsResource()
recommendation_resource = RecommendationResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    url(r'^api/', include(sms_resource.urls)),
    url(r'^api/', include(recommendation_resource.urls)),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/imag/favicon.ico')),
]
