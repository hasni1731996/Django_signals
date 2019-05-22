from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals


def create_user(sender, instance, created, **kwargs):
    print ("Object Created for User_profile Model")
class User_profile(models.Model):
    id = models.UUIDField(primary_key=True)
    user=models.ForeignKey(User,blank=True,null=True,on_delete=models.PROTECT)
    pic=models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.user.username
#####Create signals for every time an instance create for model User_profile it will called
signals.post_save.connect(receiver=create_user, sender=User_profile)

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        # model=CommonInfo
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return self.home_group

#######If we don't use Abstract=true in model's meta class than both table will create into DB# & can register separately into django's admin
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

class Users_proxy_model(User):
    class Meta:
        ordering =('username',)
        proxy =True

    def get_user_name(self):
        return Users_proxy_model.objects.filter(username='hassan')
        