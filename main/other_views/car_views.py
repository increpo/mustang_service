from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main.other_models.cars_model import Car
import datetime
from django.shortcuts import render

class CarCreate(CreateView):
    model = Car
    fields = ['owner','car_model','year_of_issue','body_serial_number','engine_serial_number']
#    initial={'create_date':'datetime.date.today()','create_user':'user.get_username'}
    template_name = 'car/car_form.html'  # Определение имени вашего шаблона и его расположения

class CarUpdate(UpdateView):
    model = Car
    fields = ['owner','car_model','year_of_issue','body_serial_number','engine_serial_number']
    template_name = 'car/car_form.html'  # Определение имени вашего шаблона и его расположения

class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('cars')
    template_name = 'car/car_confirm_delete.html'  # Определение имени вашего шаблона и его расположения

from django.views import generic
class CarListView(generic.ListView):
    model = Car
    paginate_by = 2
#    queryset = Car.objects.filter(year_of_issue__lte='2000-01-01')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'car/car_list.html'  # Определение имени вашего шаблона и его расположения

class CarDetailView(generic.DetailView):
    model = Car
    template_name = 'car/car_detail.html'  # Определение имени вашего шаблона и его расположения

    def car_detail_view(request,pk):
        try:
            car_id=Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404("Car does not exist")

        #car_id=get_object_or_404(Car, pk=pk)

        return render(
            request,
            'car/car_detail.html',
            context={'car':car_id,}
        )
