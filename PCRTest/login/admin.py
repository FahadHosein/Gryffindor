from django.contrib import admin
from .models import appt

admin.site.site_header = 'PCR Testing Facility Admin Website'
#admin.site.register(appt)


@admin.register(appt)
class apptadmin(admin.ModelAdmin):
    list_display = ('appdate','apptime','apprequest','appconfirmed','tested','result','covnow')
    ordering = ('appdate',)
    list_filter = ('apprequest','appconfirmed','tested','result','covnow')
