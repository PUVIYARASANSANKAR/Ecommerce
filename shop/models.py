from django.db import models
import datetime as dt
import os

def getfilename(request,filename):
    now_time=dt.datetime.now().strftime('%Y%m%d%H:%M:%S')
    new_filename='%s%s'%(now_time,filename)
    return os.path.join('uploads/',new_filename)

#main table
class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#product table
class Product(models.Model):
    catagory=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    quantity=models.FloatField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

