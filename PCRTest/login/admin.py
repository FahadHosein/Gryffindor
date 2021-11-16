from django.contrib import admin
from .models import appt

admin.site.site_header = 'PCR Testing Facility Admin Website'
#admin.site.register(appt)


@admin.register(appt)
class apptadmin(admin.ModelAdmin):
    
    list_display = ('requesttime','appdate','apptime','fname','lname','apprequest','appconfirmed','tested','result')
    search_fields = ('fname','lname')
    ordering = ('-requesttime',)
    list_filter = ('apprequest','appconfirmed','tested','result')
    
