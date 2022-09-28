from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=100)
    std = models.IntegerField()
    section = models.CharField(max_length=2)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length = 12)
    blood_group = models.CharField(max_length=3)

    def __str__(self):
        return self.name

