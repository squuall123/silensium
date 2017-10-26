from django.shortcuts import render

def philosophie(request):
	return render(request, 'informations/philosophie.html')