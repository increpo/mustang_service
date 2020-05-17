from django.shortcuts import render

# Create your views here.


from .other_models.cars_model import Car
from .other_models.services_model import Service
from .other_models.spares_model import Spare
from .other_models.instruments_model import Instrument
from .other_models.actions_model import Action

def Main(request):
    """
    Функция отображения для страницы Main.
    """
    # Генерация "количеств" некоторых главных объектов
#    num_cars=Car.objects.all().count()
#    num_services=Service.objects.count() # Метод 'all()' применен по умолчанию.

    old_cars=Car.objects.filter(year_of_issue__lte='2000-01-01').count()
    yang_cars=Car.objects.filter(year_of_issue__gt='2000-01-01').count()
    ending_spares=Spare.objects.filter(quantity__lte=2)
    count_ending_spares=Spare.objects.filter(quantity__lte=2).count()
    ending_instruments=Instrument.objects.filter(quantity__lt=1)
    count_ending_instruments=Instrument.objects.filter(quantity__lt=1).count()
    count_on_maintanance=Action.objects.filter(operation_finish_date=None).count()
    on_maintanance=Action.objects.filter(operation_finish_date=None)
    count_waiting_in_line=Action.objects.filter(operation_start_date=None).count()
    waiting_in_line=Action.objects.filter(operation_start_date=None)

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'main.html',
        context={'ending_spares':ending_spares,
            'count_ending_spares':count_ending_spares,
            'ending_instruments':ending_instruments,
            'num_authorscount_ending_instruments':count_ending_instruments,
            'count_ending_instruments':count_ending_instruments,
            'on_maintanance':on_maintanance,
            'count_on_maintanance':count_on_maintanance,
            'waiting_in_line':waiting_in_line,
            'count_waiting_in_line':count_waiting_in_line,
        },
    )
