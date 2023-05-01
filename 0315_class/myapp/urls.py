from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    path('index/<str:nick>',views.index,name='index'),
    path('greeting/',views.greeting,name='greeting')
]