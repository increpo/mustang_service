from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

#def index(request):
#    return render(request, 'main/index.html')

# Вызываем модели для получения данных
from .other_models.cars_model import Car
from .other_models.services_model import Service
from .other_models.spares_model import Spare
from .other_models.instruments_model import Instrument
from .other_models.actions_model import Action

def index(request):
    """
    Функция отображения для страницы Main.
    """
    # Генерация "количеств" некоторых главных объектов
#    num_cars=Car.objects.all().count()
#    num_services=Service.objects.count() # Метод 'all()' применен по умолчанию.

    old_cars=Car.objects.filter(year_of_issue__lte='2000-01-01').count()
    yang_cars=Car.objects.filter(year_of_issue__gt='2000-01-01').count()
    ending_spares=Spare.objects.filter(quantity__lte=2)[:5]
    count_ending_spares=Spare.objects.filter(quantity__lte=2).count()
    ending_instruments=Instrument.objects.filter(quantity__lt=1)[:5]
    count_ending_instruments=Instrument.objects.filter(quantity__lt=1).count()
    count_on_maintanance=Action.objects.filter(operation_finish_date=None).count()
    on_maintanance=Action.objects.filter(operation_finish_date=None)[:5]
    count_waiting_in_line=Action.objects.filter(operation_start_date=None).count()
    waiting_in_line=Action.objects.filter(operation_start_date=None)[:5]

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'main/index.html',
        context={
            'ending_spares':ending_spares,
            'count_ending_spares':count_ending_spares,
            'ending_instruments':ending_instruments,
            'count_ending_instruments':count_ending_instruments,
            'on_maintanance':on_maintanance,
            'count_on_maintanance':count_on_maintanance,
            'waiting_in_line':waiting_in_line,
            'count_waiting_in_line':count_waiting_in_line,
            'num_visits':num_visits,  # num_visits appended
        },
    )

from django.views import generic

class ActionListView(generic.ListView):
    model = Action
    context_object_name = 'on_maintanance'   # ваше собственное имя переменной контекста в шаблоне
    queryset = Action.objects.filter(operation_finish_date=None)[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'main/action_list.html'  # Определение имени вашего шаблона и его расположения

class CarListView(generic.ListView):
    model = Car
    paginate_by = 2
#    context_object_name = 'car-detail'   # ваше собственное имя переменной контекста в шаблоне
#    queryset = Car.objects.filter(year_of_issue__lte='2000-01-01')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
#    template_name = 'main/car_detail.html'  # Определение имени вашего шаблона и его расположения

class CarDetailView(generic.DetailView):
    model = Car

    def car_detail_view(request,pk):
        try:
            car_id=Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404("Car does not exist")

        #car_id=get_object_or_404(Car, pk=pk)

        return render(
            request,
            'main/car_detail.html',
            context={'car':car_id,}
        )
