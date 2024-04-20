from django import forms

from customer.models import Customer


class StyleFormMixin:
    """Миксин для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class CustomerForm(StyleFormMixin, forms.ModelForm):
    """Форма для модели Customer"""

    class Meta:
        model = Customer
        fields = "__all__"
