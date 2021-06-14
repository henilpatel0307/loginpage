from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Table1(models.Model):
    emp_nm = models.CharField("Employee Name",default="",blank=True,null=True,max_length=200)
    emp_id = models.PositiveBigIntegerField("Emploee IDS",default=0)
    emp_em = models.EmailField("Emploee Email ID",default="",blank=True,null=True,max_length=200)
    emp_cno = models.IntegerField("Employee Contact Number",default=0)
    emp_add1 = models.TextField("Employee Address1",default=0)
    emp_add2 = models.TextField("Employee Address2",default=0)

    def __str__(self):
        return self.emp_nm
