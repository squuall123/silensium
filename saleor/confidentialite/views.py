from django.shortcuts import render

def confidentialite(request):
	return render(request, 'informations/confidentialite.html')