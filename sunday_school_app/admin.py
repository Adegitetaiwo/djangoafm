from django.contrib import admin
from .models import englishSchoolA, frenchSchoolA, yorubaSchoolI
from .models import yorubaSchoolA, englishSchoolI, frenchSchoolI, elementarySchool
# Register your models here.

admin.site.register(englishSchoolA)
admin.site.register(frenchSchoolA)
admin.site.register(yorubaSchoolI)
admin.site.register(englishSchoolI)
admin.site.register(frenchSchoolI)
admin.site.register(elementarySchool)
admin.site.register(yorubaSchoolA)