from django.contrib import admin
from .models import register,order,Department,Course,material,purpose
# Register your models here.
admin.site.register(register)
admin.site.register(order)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(material)
admin.site.register(purpose)
