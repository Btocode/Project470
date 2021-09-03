from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Doctor, Hospital, Field, Disease
from django.db.models import Q


def home(request):
    return render(request, 'medicalapp/home.html')


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
