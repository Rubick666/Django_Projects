from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse

# Create your views here.


def recipes(request):
    if request.method == "POST":
        data = request.POST

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name,
            recipe_description = recipe_description,
        )
        return redirect("/")
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, "recipes.html", context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/")

def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect("/")
    context = {'recipe': queryset}
    return render(request, "update_recipe.html", context)