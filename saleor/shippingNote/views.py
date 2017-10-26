from django.shortcuts import render

def shippingNote(request):
	return render(request, 'informations/shippingNote.html')