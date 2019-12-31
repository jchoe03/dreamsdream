from django.shortcuts import render
from django.views.generic import ListView, DetailView
from school.models import School
# Create your views here.

class SchoolLV(ListView):
    model = School

class SchoolDV(DetailView):
    model = School

