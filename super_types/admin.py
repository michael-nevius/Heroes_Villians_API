from django.contrib import admin
from super_types.models import SuperType
from supers.models import Super

admin.site.register(Super)
admin.site.register(SuperType)

