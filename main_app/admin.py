from django.contrib import admin
from .models import displaySilder, setCountdownDate, userType
from .models import urgentMessage, sermonUpdate, event, subcribe
# Register your models here.

admin.site.register(displaySilder)
admin.site.register(setCountdownDate)
admin.site.register(userType)
admin.site.register(urgentMessage)
admin.site.register(sermonUpdate)
admin.site.register(event)
admin.site.register(subcribe)
