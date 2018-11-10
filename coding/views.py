from django.shortcuts import render

# Create your views here.


def site_index(request):
    return render(request, 'coding/coding_index.html')
