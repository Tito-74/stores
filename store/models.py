from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.


class StoreCategory(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name

class Store(models.Model):
  category = models.ForeignKey(StoreCategory, on_delete=models.PROTECT)
  book_title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  year_of_pub = models.IntegerField()
  description = models.TextField()
  received = models.IntegerField(default = 0, blank =True)
  issued = models.IntegerField(default = 0, blank =True)
  quantity = models.IntegerField(default = 0, blank =True)
  status = models.CharField(max_length=50)
  created_by = models.ForeignKey(User, on_delete= models.PROTECT)
  created = created = models.DateTimeField(auto_now_add=True)
  DisplayFields = ['category','book_title','author','year_of_pub','description','received','issued','quantity','status','created_by','created']

  def __str__(self):
    return self.book_title

  # def status(self):
  #   if self.quantity >= 10:
  #     status = "good"
  #     return status
  #   elif self.quantity > 5 and self.quantity <= 10:
  #     status = "bad"
  #     return status
  #   elif self.quantity > 0 and self.quantity <= 5:
  #     status = "Critical"
  #     return status
  #   else :
  #     status = "out of stock"
  #     return status

class Author(models.Model):
  firstName = models.CharField(max_length =50)
  lastName = models.CharField(max_length =50)
  email = models.EmailField()
  dob  = models.DateTimeField()

  def __str__(self):
    Author_name = self.firstName + " " + self.lastName
    return Author_name




