from django.shortcuts import render
from .models import Student
#from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView,
 DetailView, UpdateView, DeleteView)

# Create your views here.

class HomeView(ListView):
	model = Student
	template_name = 'home.html'
	context_object_name = 'students'
	ordering = ['-id']


class Create_View(SuccessMessageMixin,CreateView):
	model = Student
	template_name = 'create.html'
	fields = '__all__'
	success_url = reverse_lazy('home')
	success_message = "You just Cretaed a new record"



class Detail_View(DetailView):
	model = Student
	template_name = 'details.html'
	context_object_name = 'students'

class Update_View(SuccessMessageMixin, UpdateView):
	model = Student
	template_name = 'update.html'
	fields = ['name', 'age', 'department', 'faculty', 'about']
	success_message = "Record Updated"


class Delete_View(SuccessMessageMixin, DeleteView):
	model = Student
	template_name = 'delete.html'
	success_url = reverse_lazy('home')
	context_object_name = 'students'
	success_message = "Deleted an existing record"
