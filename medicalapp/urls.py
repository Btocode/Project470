from django.urls import path
from django.urls.conf import include

from . import views
from .views import (DiseaseListView, DoctorDetailView, DoctorListView,
                    FieldListView, HospitalListView, SearchListView)

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('hospitals/', HospitalListView.as_view(), name='hospital-list'),
    path('speciality/', FieldListView.as_view(), name='field-list'),
    path('disease/', DiseaseListView.as_view(), name='disease-list'),
    path('search/', SearchListView.as_view(), name='search-list'),
    path('register/',views.register,name = "register"),
    path('login/',views.login,name = "login"),
    
    # path('accounts/',include("accounts.urls"))
]
