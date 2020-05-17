from django.db import models
from django.contrib.auth.models import User
import uuid # Required for unique id

# Create your models here.

class Spare(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = 	models.CharField(max_length=50, help_text="Enter spares name")
    car_model = models.CharField(max_length=50, help_text="Enter car's model for spare")
    release_date = models.DateTimeField()
    quantity = models.PositiveIntegerField(null=True)
    create_date	= models.DateTimeField(auto_now_add=True)
    create_user	= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_update_date = models.DateTimeField(auto_now=True)
    last_update_user = models.ForeignKey(User, related_name='spares_last_update_user', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.id, self.name, self.car_model, self.release_date, self.quantity)
