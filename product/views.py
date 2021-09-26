from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')
def tshirt(request):
    return render(request,'tshirt.html')
def access(request):
    return render(request,'access.html')
def anime(request):
    return render(request,'anime.html')
def funky(request):
    return render(request,'funky.html')
def sup(request):
    return render(request,'sup.html')
def music(request):
    return render(request,'music.html')
def cart(request):
    return render(request,'cart.html')
def discount(request):
    return render(request,'discount.html')
def trending(request):
    return render(request,'trending.html')
def sl(request):
    return render(request,'sl.html')
def stshirt(request):
    return render(request,'stshirt.html')
