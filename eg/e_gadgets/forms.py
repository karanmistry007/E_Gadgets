import django.forms as form
from .models import Product,Category,Brand

class ProductForm(form.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
        
class CategoryForm(form.ModelForm):
    class Meta:
        model = Category
        fields = '__all__' 

class BrandForm(form.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__' 