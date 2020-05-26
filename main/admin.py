from django.contrib import admin

# Register your models here.

from .other_models.cars_model import Car
#admin.site.register(Car)
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'year_of_issue', 'display_owner', 'body_serial_number', 'engine_serial_number', 'create_date', 'last_update_date')
#    fields = ['car_model', 'year_of_issue', 'owner', ('body_serial_number', 'engine_serial_number'), ('create_user', 'last_update_user')]
    list_filter = ('car_model', 'year_of_issue')
    fieldsets = (
        ('Info:', {
            'fields': (('car_model', 'year_of_issue'), 'owner', ('body_serial_number', 'engine_serial_number'))
        }),
        ('Administrative info:', {
            'fields': ('id', ('create_user', 'last_update_user'))
        }),
    )

from .other_models.services_model import Service
admin.site.register(Service)

from .other_models.spares_model import Spare
admin.site.register(Spare)

from .other_models.instruments_model import Instrument
admin.site.register(Instrument)

from .other_models.actions_model import Action
admin.site.register(Action)
