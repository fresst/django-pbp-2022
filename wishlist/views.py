import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from wishlist.models import BarangWishlist

# Create your views here.
# Lab 1
@login_required(login_url='/wishlist/login/') # addition in Lab 3
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    user_name = request.user.username
    context = {
        'list_barang': data_barang_wishlist,
        'nama': user_name,
        'last_login' : request.COOKIES['last_login']
    }
    return render(request, "wishlist.html", context)

#Lab 2
def show_xml(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_barang_wishlist), 
                        content_type="application/xml")

def show_json(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data_barang_wishlist), 
                        content_type="application/json")

def show_xml_by_id(request,id):
    data_barang_by_id = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_barang_by_id), 
                        content_type="application/xml")

def show_json_by_id(request,id):
    data_barang_by_id = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_barang_by_id), 
                        content_type="application/json")

#Lab 3
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # mengecek apakah form sesuai kriteria
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # mengecek di form apakah user terdaftar
        if user is not None:
            login(request, user) # melakukan login
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
#            return redirect()
            return response # mengembalikan response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login') # deleting cookie
    return redirect('wishlist:login')