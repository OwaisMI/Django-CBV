from typing import List
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from advanced_app.models import *
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class indexView(TemplateView):
    template_name = 'index.html'


# #**kwargs take any argument and its key from user, ex bar(name = 'user',age=25,...)
# # *args take any argument from user, ex bar(1,2,3) or (1)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injected_content'] = 'BASIC INJECTION'
#         return context

class SchoolListView(ListView):
    context_object_name= 'schools'
    model = School #OR just School if i imported like this (from models import *)

class SchoolDetailView(DetailView):
    
    context_object_name = 'school_detail'
    model = School
    template_name = 'advanced_app/school_details.html'
    
    

class SchoolCreateView(CreateView):
    model = School
    fields = ('name','principle','location')
    
class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name','principle')

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('advanced_app:list')

class DeletePage(TemplateView):
    template_name = 'advanced_app/school_confirm_delete.html'
    # def school_detail(request, school_id):
    #     return HttpResponse("You're looking at question %s." % school_id)

