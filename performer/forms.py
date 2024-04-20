from django import forms

from customer.forms import StyleFormMixin
from performer.models import PerformerModel


class PerformerForm(StyleFormMixin, forms.ModelForm):
    """Форма для модели PerformerModel"""

    class Meta:
        model = PerformerModel
        fields = "__all__"
