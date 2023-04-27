from django.db import models

# Create your models here.



#no 2
class User(models.Model):
    firstName=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    gender=models.CharField(max_length=1)       
    contactnum=models.CharField(max_length=15)
    createdAt=models.DateField() 



#no 3
class Category(models.Model):
    categoryName=models.CharField(max_length=100)
    categoryDesc=models.CharField(max_length=100,null=True)
    categoryStatus=models.BooleanField(default=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.categoryName 
    


#no 4
class subCategory(models.Model):
    categoryName=models.ForeignKey(Category,max_length=9,on_delete=models.CASCADE)
    subCategoryName=models.CharField(max_length=30)
    subcategoryStatus=models.BooleanField(default=True)

    class Meta:
        db_table = 'subcategory'

    def __str__(self):
        return self.subCategoryName 
    




#no 5
class Brand(models.Model):
    brandName=models.CharField(max_length=30)
    brandStatus=models.BooleanField(default=True)
    
    class Meta:
        db_table = 'brand'

    def __str__(self):
        return self.brandName 
    



#no 6
class State(models.Model):
    name=models.CharField(max_length=30)

    class Meta:
        db_table = 'state'

    def __str__(self):
        return self.name 
    






#no 7
class City(models.Model):
    cityName=models.CharField(max_length=30)
    state=models.ForeignKey(State,max_length=9,on_delete=models.CASCADE)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.cityName 
    




#no 8
class vendor_Details(models.Model):
    vendorName=models.CharField(max_length=30)
    address=models.CharField(max_length=250)
    state=models.ForeignKey(State,max_length=9,on_delete=models.CASCADE)
    city=models.ForeignKey(City,max_length=9,on_delete=models.CASCADE)
    user=models.ForeignKey(User,max_length=9,on_delete=models.CASCADE)
    pinCode=models.IntegerField()
    contactNum=models.CharField(max_length=12)
    customerSupportNumber=models.CharField(max_length=12)
    feedbackEmail=models.CharField(max_length=30)


    class Meta:
        db_table = 'vendor_details'

    def __str__(self):
        return self.vendorName 
    





#no 9
class customer_Address(models.Model):
    user=models.ForeignKey(User,max_length=9,on_delete=models.CASCADE)
    adress=models.CharField(max_length=250)
    state=models.ForeignKey(State,max_length=9,on_delete=models.CASCADE)
    city=models.ForeignKey(City,max_length=9,on_delete=models.CASCADE)
    pinCode=models.IntegerField()
    isDefault=models.IntegerField()

    class Meta:
        db_table = 'customer_address'

    def __str__(self):
        return self.user





#no 10
class Product(models.Model):
    productName = models.CharField(max_length=100)
    productBrand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    productPrice = models.FloatField()
    productQty  = models.IntegerField()
    productImage1 = models.FileField(upload_to='upload/',null=True)
    productImage2 =models.FileField(upload_to='upload1/',null=True)
    productImage3 =models.FileField(upload_to='upload1/',null=True)
    productCategory=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    productDesc = models.CharField(max_length=500,null=True)
    productStatus = models.BooleanField(default=True)
    productColor = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.productName
    

# class Comind(models.Model):
#     name = models.CharField(max_length=20)

#     class Meta:
#         db_table = 'comind'







#no 11
class vendor_Product(models.Model):
    product=models.ForeignKey(Product,max_length=9,on_delete=models.CASCADE)
    vendor=models.ForeignKey(vendor_Details,max_length=9,on_delete=models.CASCADE)
    qty=models.IntegerField()
    price=models.FloatField()

    class Meta:
        db_table = 'vendor_product'

    def __str__(self):
        return self.product







#no 12
class Cart(models.Model):
    user=models.ForeignKey(User,max_length=9,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField()
    

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return self.user
    




#no 13
class Status(models.Model):
    status=models.CharField(max_length=20)
    
    class Meta:
        db_table = 'status'

    def __str__(self):
        return self.status
    

    
    

#no 14
class Order(models.Model):
    user=models.ForeignKey(User,max_length=9,on_delete=models.CASCADE)
    total=models.IntegerField()
    status=models.ForeignKey(Status,max_length=9,on_delete=models.CASCADE)
    address=models.ForeignKey(customer_Address,max_length=9,on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.user
    





#no 15
class order_Details(models.Model):
    order=models.ForeignKey(Order,max_length=9,on_delete=models.CASCADE)
    user=models.ForeignKey(User,max_length=9,on_delete=models.CASCADE)
    total=models.IntegerField()
    qty=models.IntegerField()
    price=models.FloatField()
    vendor_product=models.ForeignKey(vendor_Product,max_length=9,on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_details'

    def __str__(self):
        return self.order



#no16


#no 17
class vendor_product_Images(models.Model):
    vendor_product=models.IntegerField()
    vendor=models.IntegerField()
    imageUrl=models.CharField(max_length=500)

    class Meta:
        db_table = 'vendor_product_images'

    def __str__(self):
        return self.vendor_product



#no 18
class Feedback(models.Model):
    type=models.CharField(max_length=1)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=500)
    user=models.IntegerField()
    vendor=models.IntegerField()
    resolve=models.IntegerField()
    createdAt=models.DateField()
    vendorsAns=models.CharField(max_length=500)
    adminAns=models.CharField(max_length=600)

    class Meta:
        db_table='feedback'

    def __str__(self):
        return self.type



#test
# class AddFile(models.Model):
#     name = models.CharField(max_length=100)
#     file = models.FileField(upload_to='upload/')
    
#     class Meta:
#         db_table ='addfile'