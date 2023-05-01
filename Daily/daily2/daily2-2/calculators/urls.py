from django.urls import path
from calculators import views

app_name = 'calculators'

urlpatterns = [
    path('calculator/<int:num1>/<int:num2>',views.calculator),
]
