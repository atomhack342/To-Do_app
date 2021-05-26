
from django.urls import path 

# importing all the views manually
from .views import *
from . import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.Notes, name='notes'),
    path('delete_document/<int:docid>/', views.delete_document, name='delete_document'),

    path('calendar/', views.Calendar, name='calendar')

]