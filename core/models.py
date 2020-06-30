from django.db import models

class ID(models.Model):
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.number


class Client(models.Model):
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    email = models.EmailField(null=True,blank=True)
    photo = models.ImageField(null=True,blank=True,upload_to='clients')
    dt_birth = models.DateField(null=True,blank=True)
    doc_id = models.OneToOneField(ID,null=True,on_delete=models.CASCADE)

    def get_fullname(self):
        return self.name + ' ' + self.last_name

    def __str__(self):
        return self.get_fullname()

class Sale(models.Model):
    sale_number = models.CharField(max_length=10)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return self.sale_number
# Create your models here.
