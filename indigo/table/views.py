from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import CompanyForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# import logging
from django.core import serializers

# logger = logging.getLogger(__name__)



class SortView(generic.ListView):
    template_name = 'table/index.html'
    context_object_name = 'all_table'

    def get_queryset(self):
        return Company.objects.order_by('rank')
    

def index(request, sort_data):
    all_table = Company.objects.order_by(sort_data)
    context = {'all_table': all_table}
    if str(sort_data).startswith('-'):
        return render(request, 'table/index.html', context)
    else:
        return render(request, 'table/index_minus_sorted.html', context)

def download(request):
    qs = Company.objects.all()
    qs_json = serializers.serialize('json', qs)
    return HttpResponse(qs_json, content_type='application/json')

class CompanyCreate(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['rank', 'employer', 'employeesCount', 'medianSalary']
    template_name = 'table/new_company.html'
    

class CompanyDetail(DetailView):
    model = Company
    template_name = 'table/detail.html'

class CompanyEdit(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['rank', 'employer', 'employeesCount', 'medianSalary']
    template_name = 'table/company_edit.html'


class CompanyDelete(LoginRequiredMixin, DeleteView):
    model = Company
    success_url = reverse_lazy('index')
