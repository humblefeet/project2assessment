from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView
from .forms import WidgetForm,Form
from . import models
from .models import Widget

# Create your views here.

def base(request):
    widget_form = WidgetForm()
    widgets = Widget.objects.all()
    return render(request, 'base.html',{'widgets':  widgets ,'widget_form': widget_form})

def AddWidget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'