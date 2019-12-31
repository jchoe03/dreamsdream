from django.contrib import admin
from school.models import School

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('title','name','size','duration','image','donors')

admin.site.register(School, SchoolAdmin)
