from django.contrib import admin
from testapp.models import pune_jobs_tab,mumbai_jobs_tab

# Register your models here.
class pune_jobs_tabAdmin(admin.ModelAdmin):
    list_display=['date','company','title','elegibility','address','email','phonenumber']


class mumbai_jobs_tabAdmin(admin.ModelAdmin):
    list_display=['date','company','title','elegibility','address','email','phonenumber']

admin.site.register(pune_jobs_tab,pune_jobs_tabAdmin)
admin.site.register(mumbai_jobs_tab,mumbai_jobs_tabAdmin)
