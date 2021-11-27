
from django.contrib import admin
from django.urls import include,path
from django.views.generic import TemplateView
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('auth/', obtain_auth_token),
    path('', TemplateView.as_view(template_name='index.html')),
    
    #path('', TemplateView.as_view(template_name='index.html')),
]
