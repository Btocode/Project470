from django.contrib import admin
from .models import Disease, Field, Doctor, Hospital

# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "fields",)


admin.site.register(Disease)
admin.site.register(Field)
admin.site.register(Doctor)
admin.site.register(Hospital)
