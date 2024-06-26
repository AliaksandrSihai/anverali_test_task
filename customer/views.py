from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic

from customer.forms import CustomerForm
from customer.models import Customer
from performer.models import PerformerModel

# Create your views here.


class MainInfoView(View):
    """Отображение главной страницы"""

    def get(self, request):
        customer = Customer.objects.all()
        performer = PerformerModel.objects.all()
        context = {
            "context_customer": customer,
            "context_performer": performer,
        }
        return render(request, "customer/main.html", context)


class CustomerListView(generic.ListView):
    """Список заказчиков"""

    model = Customer
    queryset = Customer.objects.all()


class CustomerCreateView(generic.CreateView):
    """Создание нового заказчика"""

    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy("customers:all_customers")


class CustomerUpdateView(generic.UpdateView):
    """Обновление существующего заказчика"""

    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy("customers:all_customers")


class CustomerDetailView(generic.DetailView):
    """Просмотр конкретного заказчика"""

    model = Customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Customer.objects.filter(pk=self.object.pk)
        return context


class CustomerDeleteView(generic.DeleteView):
    """Удаление заказчика"""

    model = Customer
    success_url = reverse_lazy("customers:all_customers")
