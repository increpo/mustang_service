from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main.other_models.instruments_model import Instrument
import datetime
from django.shortcuts import render

class InstrumentCreate(CreateView):
    model = Instrument
    fields = '__all__'
#    initial={'create_user':'user.get_username','last_update_user':'user.get_username'}
    template_name = 'instrument/instrument_form.html'  # Определение имени вашего шаблона и его расположения

class InstrumentUpdate(UpdateView):
    model = Instrument
    fields = '__all__'
    template_name = 'instrument/instrument_form.html'  # Определение имени вашего шаблона и его расположения

class InstrumentDelete(DeleteView):
    model = Instrument
    success_url = reverse_lazy('instruments')
    template_name = 'instrument/instrument_confirm_delete.html'  # Определение имени вашего шаблона и его расположения

from django.views import generic

class InstrumentListView(generic.ListView):
    model = Instrument
    paginate_by = 2
#    queryset = Car.objects.filter(year_of_issue__lte='2000-01-01')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'instrument/instrument_list.html'  # Определение имени вашего шаблона и его расположения

class InstrumentDetailView(generic.DetailView):
    model = Instrument
    template_name = 'instrument/instrument_detail.html'  # Определение имени вашего шаблона и его расположения


    def instrument_detail_view(request,pk):
        try:
            instrument_id=Instrument.objects.get(pk=pk)
        except Instrument.DoesNotExist:
            raise Http404("Instrument does not exist")

        return render(
            request,
            'instrument/instrument_detail.html',
            context={'instrument':instrument_id,}
        )
