from django.contrib import admin
from .models import userDuty, testimony_s, firstMinister, secondMinister, thirdMinister
# Register your models here.

admin.site.register(userDuty)
admin.site.register(testimony_s)
admin.site.register(firstMinister)
admin.site.register(secondMinister)
admin.site.register(thirdMinister)

