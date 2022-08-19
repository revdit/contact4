from django.shortcuts import render

# Create your views here.
def linking_masterpage(request):
    return render(request,'linking/masterpage.html')

def linking_home(request):
    return render(request,'linking/home.html')

def linking_about(request):
    return render(request,'linking/about.html')

def linking_contact(request):
    return render(request,'linking/contact.html')