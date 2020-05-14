from django.urls import path
from . import views
app_name = 'cctv'
urlpatterns=[
    path('cctv/', views.CctvView.as_view() ,name ='home'),
]