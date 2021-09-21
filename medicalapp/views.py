from django.db.models import Q
from django.shortcuts import HttpResponse, render
from django.views.generic import DetailView, ListView

from .models import Disease, Doctor, Field, Hospital


def home_page(request):
    return render(request, 'medicalapp/home.html')

def register(request):
    
    return render(request, 'medicalapp/register.html')
def login(request):
    return render(request, 'medicalapp/login.html')

class DoctorListView(ListView):
    model = Doctor
    template_name = 'medicalapp/doctors_list.html'
    context_object_name = 'doctors'
    ordering = ['name']
    paginate_by = 10


class DoctorDetailView(DetailView):
    model = Doctor


class HospitalListView(ListView):
    model = Hospital
    template_name = 'medicalapp/hospital_list.html'
    context_object_name = 'hospitals'
    ordering = ['name']
    paginate_by = 10


class FieldListView(ListView):
    model = Field
    template_name = 'medicalapp/field_list.html'
    context_object_name = 'fields'
    ordering = ['name']
    paginate_by = 10


class DiseaseListView(ListView):
    model = Disease
    template_name = 'medicalapp/disease_list.html'
    context_object_name = 'diseases'
    ordering = ['name']
    paginate_by = 10


class SearchListView(ListView):
    model = Doctor
    template_name = 'medicalapp/search_list.html'
    ordering = ['name']
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get('q')
        # doctor_list = Doctor.objects.filter(
        #     Q(name__icontains="x") | Q(bio__icontains="x") | Q(fields__name__icontains="neuro") | Q(hospital__name__icontains="sq"))
        doctor_list = Doctor.objects.filter(Q(name__icontains=query) | Q(bio__icontains=query) | Q(
            fields__name__icontains=query) | Q(hospital__name__icontains=query) | Q(hospital__name__icontains=query) | Q(
            hospital__area__icontains=query) | Q(hospital__division__icontains=query) | Q(hospital__city__icontains=query) | Q(
            treats__name__icontains=query)).distinct()

        return doctor_list
