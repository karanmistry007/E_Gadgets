from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from .models import User
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from e_gadgets.models import Product,Category,State
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cart.cart import Cart

# Create your views here.
class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = "/user/login/"
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        username= form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
        


class UserUpdateView(UpdateView):
    model = User
    fields=('username', 'email', 'password', 'first_name','last_name','contactnum')
    template_name = 'user/user_update.html'
    success_url = "/user/user/dashboard"

class UserCheckoutView(UpdateView):
    model = User
    fields=('username', 'email', 'first_name','last_name','contactnum','address','city','zipcode','comment','state',)
    success_url = "/user/user/dashboard"
    template_name = 'user/checkout.html'
    
    def get(self, request, *args, **kwargs):
        cart=Cart(request)
        total_price = cart.get_total_price()
        context = {
        'cart': cart,
        'total_price': total_price,
        }
        return render(request,'user/checkout.html',context=context,)
   


class VendorRegisterView(CreateView):
    model = User
    form_class = VendorRegistrationForm
    template_name = 'user/vendor_register.html'
    success_url = "/user/login/"    
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        username= form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = "/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_user:
                return '/user/user/dashboard'
            else:
                return '/user/vendor/dashboard'
        

# @login_required
@method_decorator(login_required, name='dispatch')
class VendorDashboardView(ListView):      

    def get(self, request, *args, **kwargs):
        print("called....")
        input = request.GET.get('input')
        print(input)
        product=[]
        if input:
            product = Product.objects.filter(productName__icontains=input)
            print(product)
            return render(request, 'user/vendor_dashboard.html', {'product':product})
        else:
            product = Product.objects.all().values('productName','id','productPrice','productQty','productImage1','productDesc','productStatus','productColor','productCategory__categoryName','productBrand__brandName',)    
        
        return render(request, 'user/vendor_dashboard.html',{
            'product':product,
        
        })        
    template_name = 'user/vendor_dashboard.html'

# @login_required
@method_decorator(login_required, name='dispatch')
class UserDashBoardView(ListView):
    
    model = User
    


    def get(self, request, *args, **kwargs):
        print("called....")
        input = request.GET.get('input')
        print(input)
        product=[]
        if input:
            product = Product.objects.filter(productName__icontains=input)
            print(product)
            return render(request, 'user/user_dashboard.html', {'product':product})
        else:
            product = Product.objects.all().values('productName','id','productPrice','productQty','productImage1','productDesc','productStatus','productColor','productCategory__categoryName','productBrand__brandName',)    
        
        return render(request, 'user/user_dashboard.html',{
            'product':product,
        
        })        

    template_name = 'user/user_dashboard.html'


class VendorDetails(ListView):
    def get(self,request,id):
        userid = User.objects.get(id=id)
        userdetail = User.objects.all().values() 
        return render(request,'user/vendor_details.html',{'user':userdetail,'user':userid,}) 
    


      
class Home(ListView):
    def get(self, request, *args, **kwargs):
        print("called....")
        input = request.GET.get('input')
        print(input)
        product=[]
        if input:
            product = Product.objects.filter(productName__icontains=input)
            print(product)
            return render(request, 'user/home.html', {'product':product})
        else:
            product = Product.objects.all().values('productName','id','productPrice','productQty','productImage1','productDesc','productStatus','productColor','productCategory__categoryName','productBrand__brandName',) 
        
        return render(request, 'user/home.html',{
            'product':product,
        
        })        

    template_name = 'user/home.html'



#other pages
class Contact(ListView):
    def get(self, request, *args, **kwargs):
        return render(request,'user/contact.html',{})
    template_name = 'user/contact.html'


# class Cart(ListView):
#     def get(self, request, *args, **kwargs):
#         return render(request,'user/cart.html',{})
#     template_name = 'user/cart.html'


# class Checkout(ListView):
#     def get(self, request, *args, **kwargs):
#         cart=Cart(request)
#         total_price = cart.get_total_price()
#         context = {
#         'cart': cart,
#         'total_price': total_price
#         }
#         return render(request,'user/checkout.html',context=context)
#     template_name = 'user/checkout.html'
        
class About(ListView):
    def get(self,request,*args,**kwargs):
        return render(request,'user/about.html',{})
    template_name='user/about.html'
        
#cart
@login_required(login_url="/user/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="/user/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="/user/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="/user/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="/user/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="/user/login")
def cart_detail(request):
    
    cart = Cart(request)
    total_price = cart.get_total_price()
    context = {
        'cart': cart,
        'total_price': total_price
    }
    return render(request, 'user/cart.html', context=context)


    # return render(request, 'user/cart.html')
    
