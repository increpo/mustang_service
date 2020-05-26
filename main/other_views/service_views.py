from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main.other_models.services_model import Service
import datetime
from django.shortcuts import render

class ServiceCreate(CreateView):
    model = Service
    fields = '__all__'
#    initial={'create_user':'user.get_username','last_update_user':'user.get_username'}
    template_name = 'service/service_form.html'  # Определение имени вашего шаблона и его расположения

class ServiceUpdate(UpdateView):
    model = Service
    fields = '__all__'
    template_name = 'service/service_form.html'  # Определение имени вашего шаблона и его расположения

class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('services')
    template_name = 'service/service_confirm_delete.html'  # Определение имени вашего шаблона и его расположения

from django.views import generic

class ServiceListView(generic.ListView):
    model = Service
    paginate_by = 2
#    queryset = Car.objects.filter(year_of_issue__lte='2000-01-01')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    template_name = 'service/service_list.html'  # Определение имени вашего шаблона и его расположения

class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'service/service_detail.html'  # Определение имени вашего шаблона и его расположения


    def service_detail_view(request,pk):
        try:
            service_id=Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404("service does not exist")

        return render(
            request,
            'service/service_detail.html',
            context={'service':service_id,}
        )
