from django.shortcuts import render

# Create your views here.
def view_top(request):
    return render(request, 'top.html')
