from django.shortcuts import render
# Create your views here.
def showcontact(request):
    return render(request,'contactpage.html')