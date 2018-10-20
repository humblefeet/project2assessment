from .models import Widget
from django.forms import ModelForm, Form

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']

