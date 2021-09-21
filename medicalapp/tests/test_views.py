
import json

from django.db.models.query_utils import refs_expression
from django.http import response
from django.test import Client, TestCase
from django.test.testcases import TestCase
from django.urls import reverse
from medicalapp.models import Disease, Doctor, Field, Hospital


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home = reverse('home')
        self.login = reverse('login')
        self.doctor = reverse('doctor-list')
        self.hospital = reverse('hospital-list')
        self.disease = reverse('disease-list')
        self.field = reverse('field-list')
        self.search = reverse("search-list")


    def test_home(self):
        
        response = self.client.get(self.home)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicalapp/home.html')

    def test_login(self):
        
        response = self.client.get(self.login)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicalapp/login.html')
    

    def test_base(self):
        
        response = self.client.get(self.home)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicalapp/base.html')
    
    def test_doctor_list(self):
        
        response = self.client.get(self.doctor)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicalapp/doctors_list.html')


    def test_disease_list(self):
        
        response = self.client.get(self.disease)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicalapp/disease_list.html')

    def test_hospital_list(self):
        
        response = self.client.get(self.hospital)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicalapp/hospital_list.html')

    def test_field_list(self):
        
        response = self.client.get(self.field)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'medicalapp/field_list.html')

    # def test_search_list(self):
        
    #     response = self.client.get(self.search)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'medicalapp/search_list.html')
