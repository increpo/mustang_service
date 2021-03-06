from django.db import models
from django.contrib.auth.models import User
import uuid # Required for unique id
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = 	models.CharField(max_length=50, help_text="Enter service type name")
    create_date	= models.DateTimeField(auto_now_add=True)
    create_user	= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_update_date = models.DateTimeField(auto_now=True)
    last_update_user = models.ForeignKey(User, related_name='services_last_update_user',  on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return '{}, {}'.format(self.id, self.name)
    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])
