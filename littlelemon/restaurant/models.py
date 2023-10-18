from django.db import models

# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200, default='')
   last_name = models.CharField(max_length=200, default='')
   guest_number = models.IntegerField(default=1)
   comment = models.CharField(max_length=1000, default='')

   def __str__(self):
      return self.first_name.title() + ' ' + self.last_name.title()

   class Meta:
        verbose_name_plural = ("Booking")

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.name
