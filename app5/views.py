from django.shortcuts import render
# Create your views here.
def queen(request):
    return render(request,'king.html')