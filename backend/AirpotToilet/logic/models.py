from django.db import models

# Create your models here.
class Staff(models.Model):
    Sid = models.AutoField(primary_key=True)
    Sname = models.CharField(max_length=250)
    Phone = models.CharField(max_length = 10)
    Address = models.CharField(max_length=250)

class Day(models.Model):
    DAY_CHOICES = [
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    ]

    Did = models.AutoField(primary_key=True)
    Day = models.IntegerField(choices=DAY_CHOICES, unique=True)



class Allocation(models.Model):
    Aid = models.AutoField(primary_key=True)
    Sid = models.ForeignKey(Staff, on_delete = models.CASCADE)
    Did = models.OneToOneField(Day, on_delete = models.CASCADE)


class Feedback(models.Model):
    value_choice = (
        ('good', 'good'),
        ('poor', 'poor')
    )

    Fid = models.AutoField(primary_key=True)
    Value = models.CharField(max_length=10, choices=value_choice)
    Aid = models.ForeignKey(Allocation, on_delete=models.CASCADE, blank=True)