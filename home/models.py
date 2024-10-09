from django.db import models

# Create your models here.




    
class UserModel(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=25)
    email = models.EmailField()


class HouseModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    sq_meters = models.IntegerField()
    private_bath = models.BooleanField(default=False)
     