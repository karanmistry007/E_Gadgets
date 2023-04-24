from django.shortcuts import render,redirect
from .models import Product,Category,Brand
from django.http import HttpResponse
from .forms import ProductForm,CategoryForm,BrandForm
from django.conf import settings
#send mail
from django.core.mail import send_mail

from django.views.generic import CreateView
from django.views.generic import ListView,DetailView
from django.views.generic import DeleteView,UpdateView

# Create your views here.
        
    
    
def sendMail(request):
    subject = "welcome to django"
    message = "hello django"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ksmistry007@gmail.com','vrajshah1930@gmail.com']
    res = send_mail(subject,message,email_from,recipient_list)
    if res>0:
        print("mail sent")
    else:
        print("mail not sent")    
    print(res)
    return HttpResponse("mail sent")

#Product class view 
class ProjectCreationView(CreateView):
    form_class =ProductForm
    # fields = ['productName', 'productBrand', 'productPrice', 'productQty', 'productCategory','productImage' ,'productDesc', 'productStatus', 'productColor']
    model = Product
    template_name = 'product/addproduct.html'
    success_url = '/user/vendor/dashboard/'
    # def form_valid(self, form):
    #     return super().form_valid(form)

    def form_valid(self, form):
        # Save the form data to the database
        self.object = form.save(commit=False)
        self.object.productImage1 = self.request.FILES['productImage1']  # Set the image field to the uploaded file
        self.object.save()
        return super().form_valid(form)
   

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/updateproduct.html'
    success_url = '/user/vendor/dashboard/'


class ProductDeleteView(DeleteView):
    model = Product
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/user/vendor/dashboard/' 


class ProductDetailView(DetailView):
    model=Product
    template_name='product/productdetail.html'


    def get(self, request,pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        productall=Product.objects.all().values()
        return render(request,'product/productdetail.html',{'product':product,'products':productall})


#category class view

class CategoryCreationView(CreateView):
    form_class =CategoryForm
    model = Category
    template_name = 'product/addcategory.html'
    success_url = '/product/getcategories/'
    def form_valid(self, form):
        return super().form_valid(form)
    


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'product/updatecategory.html'
    success_url = '/product/getcategories/'

    
class CategoryDeleteView(DeleteView):
    model = Category    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/product/getcategories/'


class CategoryDetailView(DetailView):
    model=Category
    template_name='product/getcategories.html'

    def get(self, request, *args, **kwargs):
        category=Category.objects.all().values()
        return render(request,'product/allcategories.html',{'category':category,})
    



#brand class view

class BrandCreationView(CreateView):
    form_class =BrandForm
    model = Brand
    template_name = 'product/addbrand.html'
    success_url = '/product/getbrands/'
    def form_valid(self, form):
        return super().form_valid(form)
    


class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'product/updatebrand.html'
    success_url = '/product/getbrands/'

    
class BrandDeleteView(DeleteView):
    model = Brand    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/product/getbrands/'


class BrandDetailView(DetailView):
    model= Brand
    template_name='product/getbrands.html'

    def get(self, request, *args, **kwargs):
        brand=Brand.objects.all().values()
        return render(request,'product/allbrands.html',{'brand':brand,})
    




#cart views











#test

# class AddFileView(CreateView):
#     model = AddFile
#     template_name = 'product/addfile.html'
#     success_url = '/product/filelist'
#     fields = '__all__'



# class FileListView(ListView):
#     model = AddFile
#     template_name = 'product/filelist.html'
#     context_object_name = 'filelist'