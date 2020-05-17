from django.db import models
from django.contrib.auth.models import User
import uuid # Required for unique id
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.
class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ManyToManyField(User, related_name='owners')
    car_model = models.CharField(max_length=50, help_text="Enter car's model")
    year_of_issue =	models.DateField()
    body_serial_number = models.CharField(max_length=20)
    engine_serial_number = models.CharField(max_length=20)
    create_date	= models.DateTimeField(auto_now_add=True)
    create_user	= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_update_date = models.DateTimeField(auto_now=True)
    last_update_user = models.ForeignKey(User, related_name='cars_last_update_user', on_delete=models.SET_NULL, null=True)

    def display_owner(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ User.username for User in self.owner.all()[:3] ])
        display_owner.short_description = 'Owners'

#    def get_absolute_url(self):
    """
    Returns the url to access a particular instance of the model.
    """
#    return reverse('model-detail-view', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])

    def __str__(self):
        return '{}, {}, {}'.format(self.id, self.car_model, self.year_of_issue)
