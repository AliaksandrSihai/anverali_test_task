from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from performer.forms import PerformerForm
from performer.models import PerformerModel
# Create your views here.


class PerformerListView(generic.ListView):
    """Список исполнителей"""
    model = PerformerModel
    queryset = PerformerModel.objects.all()

class PerformerCreateView(generic.CreateView):
    """Создание нового исполнителя"""
    model = PerformerModel
    form_class = PerformerForm
    success_url = reverse_lazy("performers:all_performers")

class PerformerUpdateView(generic.UpdateView):
    """Обновление существующего исполнителя """
    model = PerformerModel
    form_class = PerformerForm
    success_url = reverse_lazy("performers:all_performers")

class PerformerDetailView(generic.DetailView):
    """Просмотр конкретного исполнителя """
    model = PerformerModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = PerformerModel.objects.filter(pk=self.object.pk)
        return context

class PerformerDeleteView(generic.DeleteView):
    """Удаление исполнителя """
    model = PerformerModel
    success_url = reverse_lazy("performers:all_performers")