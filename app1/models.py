from django.db import models

class Company_Data(models.Model):
    com_name = models.CharField(default="",max_length=200)
    com_em  = models.EmailField(default="",max_length=200)
    com_co = models.PositiveBigIntegerField(default=0)
    com_add = models.TextField(default="")
    join_date = models.DateField(auto_now=True,blank=True,null=True)
    profile = models.ImageField(upload_to="Com_Profile/",default="",max_length=400)
    com_pass = models.CharField(default="",max_length=200)

    def __str__(self):
        return self.com_name