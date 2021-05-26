
from django.urls import path 

# importing all the views manually
from .views import *
from . import views
# from django.contrib.auth.views import LogoutView


from django.conf .urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.Account, name='account')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
