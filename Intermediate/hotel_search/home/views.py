from django.shortcuts import render
from django.http import JsonResponse
from .models import *
# Create your views here.


def home(request):
    return render(request, "home.html")

def get_hotel(request):
    try:
        Ans_objs = Hotel.objects.all()
        if request.GET.get('sort_by'):
            sort_by_value = request.GET.get('sort_by')
            if sort_by_value == 'asc':
                Ans_objs = Ans_objs.order_by('price')
            elif sort_by_value == "dsc":
                Ans_objs = Ans_objs.order_by('-price')
            
            if request.GET.get('amount'):
                amount = request.GET.get('amount')
                Ans_objs = Ans_objs.filter(price__Ite = amount)
        payload = []
        for Ans_obj in Ans_objs:
            payload.append({
                'name':Ans_obj.name,
                'price': Ans_obj.price,
                'description': Ans_obj.description,
            })
        return JsonResponse(payload, safe=False)
    except Exception as e:
        print(e)
    return JsonResponse({'message': "Something went wrong!"})