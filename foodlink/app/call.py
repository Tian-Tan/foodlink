import requests
import json

def search (ingredients):
    s = "https://api.edamam.com/api/recipes/v2?type=public&q=" + ingredients + "&app_id=02b624bb&app_key=dd51796fcd6547eccd4141d1f2454ef4"
    response = requests.get(s)
    print(response.status_code)
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
