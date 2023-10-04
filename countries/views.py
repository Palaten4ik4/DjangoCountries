from django.shortcuts import render
from django.http import Http404
import json
from django.core.paginator import Paginator

def load_countries():
    with open('country-by-languages.json', 'r') as file:
        return json.load(file)

def index(request):
    return render(request, 'index.html')

def country_list(request):
    countries = load_countries()
    paginator = Paginator(countries, 10)  # Показывать 10 стран на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'country_list.html', {'page_obj': page_obj})

def country_detail(request, country_name):
    countries = load_countries()
    country = next((c for c in countries if c['country'] == country_name), None)
    if not country:
        # Ошибка 404, если страна не найдена
        raise Http404("Country not found")
    return render(request, 'country_detail.html', {'country': country}) # исправлен путь к шаблону

def countries_by_letter(request, letter):
    countries = load_countries()
    filtered_countries = [country for country in countries if country['country'].startswith(letter.upper())]
    return render(request, 'country_list.html', {'countries': filtered_countries})

def language_list(request):
    countries = load_countries()
    languages = set()
    for country in countries:
        for language in country['languages']:
            languages.add(language)
    
    return render(request, 'language_list.html', {'languages': sorted(languages)})  # исправлен путь к шаблону

def countries_by_language(request, language_name):
    countries = load_countries()
    filtered_countries = [country for country in countries if language_name in country['languages']]
    return render(request, 'country_list.html', {'countries': filtered_countries})
