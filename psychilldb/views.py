from django.shortcuts import render

# Create your views here.
def psychilldb(request):
	return render(request, 'psychilldb/base.html')
