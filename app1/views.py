from django.shortcuts import render

# Create your views here.
def green(request):
    return render(request,'green.html')
