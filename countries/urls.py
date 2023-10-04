from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries-list/', views.country_list, name='country_list'),
    path('countries-list/by-country/<str:country_name>/', views.country_detail, name='country_detail'),
    path('countries-list/by-letter/<str:letter>/', views.countries_by_letter, name='countries_by_letter'),
    path('languages/', views.language_list, name='language_list'),
    path('countries-list/by-language/<str:language_name>/', views.countries_by_language, name='countries_by_language'),
]
