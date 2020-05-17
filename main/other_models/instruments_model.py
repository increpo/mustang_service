from django.db import models
from django.contrib.auth.models import User
import uuid # Required for unique id

# Create your models here.

class Instrument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = 	models.CharField(max_length=50, help_text="Enter instrument's name")
    quantity = models.PositiveIntegerField(null=True)
    create_date	= models.DateTimeField(auto_now_add=True)
    create_user	= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_update_date = models.DateTimeField(auto_now=True)
    last_update_user = models.ForeignKey(User, related_name='instruments_last_update_user', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return '{}, {}'.format(self.id, self.name)
