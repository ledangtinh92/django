from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from apps.myapp.form.categoreForm import ProductCategoryForm
from apps.myapp.form.loginForm import LoginForm
from apps.myapp.form.productForm import ProductForm
from apps.myapp.models import Product, ProductCategory
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, '../templates/home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, '../templates/product_list.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, '../templates/add_product.html', {'form': form})


def category_list(request):
    categories = ProductCategory.objects.all()
    return render(request, '../templates/category_list.html', {'categories': categories})


def add_category(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductCategoryForm()
    return render(request, '../templates/add_category.html', {'form': form})
