from django.db import models

# Create your models here.


class Equipments(models.Model):
    Name=models.CharField(max_length=20)
    Price=models.CharField(max_length=20)
    Unit=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Description=models.CharField(max_length=100)


    def __str__(self):
        return self.Name




class Plan(models.Model):
    Name=models.CharField(max_length=20)
    Amount=models.CharField(max_length=20)
    Duration=models.CharField(max_length=20)



    def __str__(self):
        return self.Name

class Contact(models.Model):
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Contact=models.CharField(max_length=20)
    Email_Id=models.CharField(max_length=50)
    Age=models.CharField(max_length=20)
    Describe=models.TextField()




    def __str__(self):
        return self.First_Name



class Member(models.Model):
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Contact=models.CharField(max_length=20)
    Email_Id=models.CharField(max_length=50)
    Age=models.CharField(max_length=20)





    def __str__(self):
        return self.First_Name