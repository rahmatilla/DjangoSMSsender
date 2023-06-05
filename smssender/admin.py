from django.contrib import admin
from .models import SMSReceiver, SMSlog, AlarmReport

class SMSReceiverAdmin(admin.ModelAdmin):
    list_display = ('network', 'criteria', 'notification', 'tel_number', 'name', 'created_at', 'updated_at')

admin.site.register(SMSReceiver, SMSReceiverAdmin)

class SMSlogAdmin(admin.ModelAdmin):
    list_display = ('source_addr', 'sms_text', 'tel_number_list', 'user', 'sent_time')

admin.site.register(SMSlog, SMSlogAdmin)

class AlarmReportAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AlarmReport._meta.fields if field.name != "id"]

admin.site.register(AlarmReport, AlarmReportAdmin)
