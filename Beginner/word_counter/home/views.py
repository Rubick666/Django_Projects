from django.shortcuts import render
import translate
# Create your views here.
def counter(request):
    if request.method == "POST":
        text = request.POST['texttocount']
        if text != '':
            word = len(text.split())
            i = True
            return render(request, "counter.html",
                          {'word': word, 'text':text, 'i':i, 'on':'active'})
        else:
            return render(request, 'counter.html', {'on':'active'})
        
    else:
        return render(request, "counter.html", {'on':'active'})

def home(request):
    return render(request, "counter.html", {'on':'active'})