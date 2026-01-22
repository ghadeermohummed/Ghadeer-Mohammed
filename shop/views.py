from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import *
from django.contrib import messages
def index(request):
    return  render(request,"html/index.html")

def about(request):
    return  render(request,"html/about.html")

def contact(request):
    return  render(request,"html/contact.html")

@login_required(login_url='login')
def cart(request):
    return  render(request,"html/cart.html")


@login_required(login_url='login')
def service(request):
    return  render(request,"html/service.html")

@login_required(login_url='login')
def product(request):
    product=Product.objects.all()
    return  render(request,"html/product.html",{"product":product})

def gallery(request):
    return  render(request,"html/gallery.html")


def signup(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignForm()
    return render(request, "html/signup.html", {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_input = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # جرّب username مباشرة
            user = authenticate(request, username=login_input, password=password)

            # لو فشل، جرّب email
            if user is None:
                try:
                    user_obj = User.objects.get(email=login_input)
                    user = authenticate(
                        request,
                        username=user_obj.username,
                        password=password
                    )
                except User.DoesNotExist:
                    user = None

            if user:
                auth_login(request, user)

                # أدمن → داشبورد
                if user.is_staff or user.is_superuser:
                    return redirect('indexDash')

                # مستخدم عادي → الرئيسية
                return redirect('index')

            messages.error(request, "البيانات غير صحيحة")
    else:
        form = LoginForm()

    return render(request, "html/login.html", {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')

def is_admin(user):
    return user.is_staff

@login_required(login_url='login')
@user_passes_test(is_admin)
def indexDash(request):
    return render(request, 'dashboard/indexDash.html')

@login_required(login_url='login')
@user_passes_test(is_admin)
def add_a_product(request):
    form=ProductForm()
    if request.method == 'POST':
         form=ProductForm(request.POST,request.FILES)
         if form.is_valid():
            form.save()
            messages.success(request,'added successflly ...')
            return redirect('list_product')
         
    return render(request, 'dashboard/add-a-product.html',{'form':form})


@login_required(login_url='login')
@user_passes_test(is_admin)
def edit_a_product(request,Pk):
    product=Product.objects.get(ID=Pk)
    form=ProductForm(instance=product)
    if request.method == 'POST':
         form=ProductForm(request.POST,request.FILES,instance=product)
         if form.is_valid():
            form.save()
            messages.success(request,'edit successflly ...')
            return redirect('list_product')
         else:
            form=ProductForm()
    return render(request, 'dashboard/edit-a-product.html',{'form':form})
 

@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_product(request,Pk):
    product=Product.objects.get(ID=Pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request,'deleted successflly ...')
        return redirect('list_product')
    return render(request, 'dashboard/Delete-product.html',{'product':product})

@login_required(login_url='login')
@user_passes_test(is_admin)
def list_product(request):
    product=Product.objects.all()
    return render(request, 'dashboard/listProduct.html',{'all_product':product})


@login_required(login_url='login')
@user_passes_test(is_admin)
def add_a_customer(request):
    form=CustomerForm()
    if request.method == 'POST':
         form=CustomerForm(request.POST)
         if form.is_valid():
            form.save()
            messages.success(request,'added successflly ...')
            return redirect('list_customer')
         
    return render(request, 'dashboard/add-a-customer.html',{'form':form})

@login_required(login_url='login')
@user_passes_test(is_admin)
def edit_a_customer(request,Pk):
    customer=Customer.objects.get(ID=Pk)
    form=CustomerForm(instance=customer)
    if request.method == 'POST':
         form=CustomerForm(request.POST,instance=customer)
         if form.is_valid():
            form.save()
            messages.success(request,'edit successflly ...')
            return redirect('list_customer')
         else:
            form=CustomerForm()
    return render(request, 'dashboard/edit-a-customer.html',{'form':form})
 
@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_customer(request,Pk):
    customer=Customer.objects.get(ID=Pk)
    if request.method == 'POST':
        customer.delete()
        messages.success(request,'deletd successflly ...')
        return redirect('list_customer')
    return render(request, 'dashboard/Delete-customer.html',{'customer':customer})

@login_required(login_url='login')
@user_passes_test(is_admin)
def list_customer(request):
    customer=Customer.objects.all()
    return render(request, 'dashboard/listCustomer.html',{'all_customer':customer})

@login_required(login_url='login')
@user_passes_test(is_admin)
def add_a_order(request):
    form=OrderForm()
    if request.method == 'POST':
         form=OrderForm(request.POST)
         if form.is_valid():
            form.save()
            messages.success(request,'added successflly ...')
            return redirect('list_order')
         else:
            form=OrderForm()
    return render(request, 'dashboard/add-a-order.html',{'form':form})

@login_required(login_url='login')
@user_passes_test(is_admin)
def edit_a_order(request,Pk):
    order=Order.objects.get(ID=Pk)
    form=OrderForm(instance=order)
    if request.method == 'POST':
         form=OrderForm(request.POST,instance=order)
         if form.is_valid():
            form.save()
            messages.success(request,'edit successflly ...')
            return redirect('list_order')
         else:
            form=OrderForm()
    return render(request, 'dashboard/edit-a-order.html',{'form':form})
 
@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_order(request,Pk):
    order=Order.objects.get(ID=Pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request,'deletd successflly ...')
        return redirect('list_order')
    return render(request, 'dashboard/Delete-order.html',{'order':order})

@login_required(login_url='login')
@user_passes_test(is_admin)
def list_order(request):
    order=Order.objects.all()
    return render(request, 'dashboard/listOrder.html',{'all_order':order})

@login_required(login_url='login')
@user_passes_test(is_admin)
def add_a_orderitem(request):
    form=OrderItemForm()
    if request.method == 'POST':
         form=OrderItemForm(request.POST)
         if form.is_valid():
            form.save()
            messages.success(request,'added successflly ...')
            return redirect('list_orderitem')
         else:
            form=OrderItemForm()
    return render(request, 'dashboard/add-a-orderitem.html',{'form':form})

@login_required(login_url='login')
@user_passes_test(is_admin)
def edit_a_orderitem(request,Pk):
    orderitem=OrderItem.objects.get(ID=Pk)
    form=OrderItemForm(instance=orderitem)
    if request.method == 'POST':
         form=OrderItemForm(request.POST,instance=orderitem)
         if form.is_valid():
            form.save()
            messages.success(request,'edit successflly ...')
            return redirect('list_orderitem')
         else:
            form=OrderItemForm()
    return render(request, 'dashboard/edit-a-orderitem.html',{'form':form})

@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_orderitem(request,Pk):
    orderitem=OrderItem.objects.get(ID=Pk)
    if request.method == 'POST':
        orderitem.delete()
        messages.success(request,'deletd successflly ...')
        return redirect('list_orderitem')
    return render(request, 'dashboard/Delete-orderitem.html',{'orderitem':orderitem})


@login_required(login_url='login')
@user_passes_test(is_admin)
def list_orderitem(request):
    orderitem=OrderItem.objects.all()
    return render(request, 'dashboard/listOrderitem.html',{'all_orderitem':orderitem}) 

def pages_blank(request):
    return render(request, 'dashboard/pages-blank.html')

def pages_profile(request):
    return render(request, 'dashboard/pages-profile.html')

def pages_sign_in(request):
    return render(request, 'dashboard/pages-sign-in.html')

def pages_sign_up(request):
    return render(request, 'dashboard/pages-sign-up.html')

def upgrade_to_pro(request):
    return render(request, 'dashboard/upgrade-to-pro.html')

# Pages mostly used as components/includes
def base(request):
    return render(request, 'dashboard/base.html')

def footerDash(request):
    return render(request, 'dashboard/footerDash.html')

def navDash(request):
    return render(request, 'dashboard/navDash.html')

def sideDash(request):
    return render(request, 'dashboard/sideDash.html')

def charts_chartjs(request):
    return render(request, 'dashboard/charts-chartjs.html')

def maps_google(request):
    return render(request, 'dashboard/maps-google.html')

def icons_feather(request):
    return render(request, 'dashboard/icons-feather.html')



