from django.shortcuts import render
from django.http import HttpResponse
#helper functions are in views.py because django is weird
import requests
import json

def search(ingredients):
    s = "https://api.edamam.com/api/recipes/v2?type=public&q=" + ingredients + "&app_id=02b624bb&app_key=dd51796fcd6547eccd4141d1f2454ef4"
    try:
        response = requests.get(s)
    except:
        return None
    #print(response.status_code)
    r1 = get_everything(response, 0)
    r2 = get_everything(response, 1)
    r3 = get_everything(response, 2)
    r4 = get_everything(response, 3)
    r5 = get_everything(response, 4)
    recipies = [r1, r2, r3, r4, r5]
    return recipies
    
    
def get_calories(response, n):
    return response.json()["hits"][n]["recipe"]["calories"]


def get_label(response, n):
    return response.json()["hits"][n]["recipe"]["label"]
    

def get_ingredients(response, n):
    return response.json()["hits"][n]["recipe"]["ingredientLines"]

def get_image(response, n):
    return response.json()["hits"][n]["recipe"]["image"]


def get_url(response, n):
    return response.json()["hits"][n]["recipe"]["url"]


def get_everything(response, n):
    return {"label": get_label(response, n), "ingredients": get_ingredients(response, n), 
             "calories": get_calories(response, n), "url": get_url(response, n), "image": get_image(response, n)}
#image, nutrition, name, ingredients, url

# Create your views here.

def home_view(request, *args, **kargs):
    if request.method == 'POST':
        user_input = request.POST.get('search')
        recipes = search(str(user_input))
        if recipes == None:
            return render(request, 'error.html', {})
        else:
            context = {
            "1_name": recipes[0]['label'],
            "1_image": recipes[0]['image'],
            "1_ingredients": recipes[0]['ingredients'], #list
            "1_info": recipes[0]['url'],
            "1_calories": recipes[0]['calories'],
            "2_name": recipes[1]['label'],
            "2_image": recipes[1]['image'],
            "2_ingredients": recipes[1]['ingredients'], #list
            "2_info": recipes[1]['url'],
            "2_calories": recipes[1]['calories'],
            "3_name": recipes[2]['label'],
            "3_image": recipes[2]['image'],
            "3_ingredients": recipes[2]['ingredients'], #list
            "3_info": recipes[2]['url'],
            "3_calories": recipes[2]['calories'],
            "4_name": recipes[3]['label'],
            "4_image": recipes[3]['image'],
            "4_ingredients": recipes[3]['ingredients'], #list
            "4_info": recipes[3]['url'],
            "4_calories": recipes[3]['calories'],
            "5_name": recipes[4]['label'],
            "5_image": recipes[4]['image'],
            "5_ingredients": recipes[4]['ingredients'], #list
            "5_info": recipes[4]['url'],
            "5_calories": recipes[4]['calories'],
            }
            return render(request, 'results.html', context)
    return render(request, 'index.html', {})

def about_view(request, *args, **kargs):
    return render(request, 'aboutUs.html', {})
'''
def result_view(request, *args, **kargs):
    return render(request, 'results.html', {})
'''
def error_view(request, *args, **kargs):
    return render(request, 'error.html', {})

def foodbank_view(request, *args, **kargs):
    return render(request, 'foodbank.html', {})

def resources_view(request, *args, **kargs):
    return render(request, 'resources.html', {})