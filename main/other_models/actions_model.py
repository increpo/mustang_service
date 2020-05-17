from django.db import models
from django.contrib.auth.models import User
import uuid # Required for unique id

# Create your models here.

class Action(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    car_id  = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)
    user_staff_id = models.ForeignKey(User, related_name='user_staff_id', on_delete=models.SET_NULL, null=True)
    user_client_id = models.ForeignKey(User, related_name='user_client_id', on_delete=models.SET_NULL, null=True)
    service_id = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True)
    operation_start_date = models.DateTimeField()
    operation_finish_date = models.DateTimeField()
    spare_id = models.ForeignKey('Spare', on_delete=models.SET_NULL, null=True)
    instrument_id = models.ForeignKey('Instrument', on_delete=models.SET_NULL, null=True)
    create_date	= models.DateTimeField(auto_now_add=True)
    create_user	= models.ForeignKey(User, related_name='create_user', on_delete=models.SET_NULL, null=True)
    last_update_date = models.DateTimeField(auto_now=True)
    last_update_user = models.ForeignKey(User, related_name='actions_last_update_user', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('action-detail', args=[str(self.id)])

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.id, self.car_id, self.user_staff_id, self.service_id)
