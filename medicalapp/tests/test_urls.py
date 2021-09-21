from django.test.testcases import TestCase
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from medicalapp.views import (DiseaseListView, DoctorDetailView,
                              DoctorListView, HospitalListView, home_page,
                              login, register,FieldListView,SearchListView)


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func,home_page)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func,login)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func,register)
    
    def test_doctorList_url_is_resolved(self):
        url = reverse('doctor-list')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,DoctorListView)

    def test_hospital_url_is_resolved(self):
        url = reverse('hospital-list')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,HospitalListView)

    def test_disease_url_is_resolved(self):
        url = reverse('disease-list')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,DiseaseListView)

    def test_fields_url_is_resolved(self):
        url = reverse('field-list')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,FieldListView)


    def test_search_url_is_resolved(self):
        url = reverse('search-list')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,SearchListView)