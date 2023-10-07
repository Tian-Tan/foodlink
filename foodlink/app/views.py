from django.shortcuts import render
from django.http import HttpResponse
from call import search
# Create your views here.

def home_view(request, *args, **kargs):
    if request.method == 'POST':
        user_input = request.POST.get('search')
        recipes = search(str(user_input))
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
        return render(request, 'recipe.html', context)
    return render(request, 'index.html', {})