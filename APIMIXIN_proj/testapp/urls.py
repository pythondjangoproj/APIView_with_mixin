# from django.contrib import admin
from django.urls import path
from testapp import views

app_name='testapp'
urlpatterns = [
    path('api/',views.EmployeeListCreateModelMixin.as_view()),
    path('api/<pk>',views.EmployeeRetriveUpdateDestroyModelMixin.as_view()),

]