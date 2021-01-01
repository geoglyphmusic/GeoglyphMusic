from django.shortcuts import render

# Create your views here.
def psychillworld(request):
    return render(request, 'psychillworld/psychillworld.html')
