from django.db import models

# Create your models here.
class Category(models.Model):
    Name=models.CharField(max_length=20)
    def __str__(self):
        return self.Name


class Product(models.Model):
    Name=models.CharField(max_length=50)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    Image=models.ImageField(upload_to='img')
    Desc=models.TextField()
    Price=models.IntegerField()
    def __str__(self):
        return self.Name
    #static method
    @staticmethod
    def get_category_id(get_id):
        if get_id:
            return Product.objects.filter(Category=get_id)
        else:
            return Product.objects.all()
class Customer(models.Model):
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Email=models.EmailField(unique=True)
    Phone=models.CharField(max_length=10)
    Password=models.CharField(max_length=200)
    #checking if email is existing or not
    def isexist(self):
        if Customer.objects.filter(Email=self.Email):
            return True
        return False
    def phoneexist(self):
        if Customer.objects.filter(Phone=self.Phone):
            return True
        return False

    @staticmethod
    def getemail(email):
        try:
            return Customer.objects.get(Email=email)
        except:
            return False