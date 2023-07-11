from django.db import models

from django.urls import reverse

# Create your models here.
class Frog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age=models.IntegerField()

    # returns a readable representation of
    # an instance of an object
    def __str__(self):
        return f'{self.name} ({self.id})'

    # calculates the url automatically
    # pass in self, an instance of the class for this model
    # frog_id is the variable in routes/controller
    def get_absolute_url(self):
        return reverse('detail', kwargs={'frog_id': self.id})
