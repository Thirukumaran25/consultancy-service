from django.contrib import admin
from .models import Job,Company, BotQuestion

# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'job_title',
        'company_name',
        'location',
        'experience',
        'salary_range',
        'posted_at'
    )
    search_fields = ('job_title', 'company_name', 'location')
    list_filter = ('location',)


admin.site.register(Company)
admin.site.register(BotQuestion)