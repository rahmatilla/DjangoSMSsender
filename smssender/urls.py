from django.urls import path
from .views import SMSReceiverView, SMSlogView, SMSReceiverRetrive, SendSMS, SMSSend, AlarmReportView, AlarmReportRetrive


urlpatterns = [
    path('smsreceiver/', SMSReceiverView.as_view()),
    path('smsreceiver/<int:pk>/', SMSReceiverRetrive.as_view()),
    path('alarmreport/', AlarmReportView.as_view()),
    path('alarmreport/<int:pk>/', AlarmReportRetrive.as_view()),
    path('smslog/', SMSlogView.as_view()),
    path('sendsms/', SendSMS.as_view()),
    path('smssend/', SMSSend.as_view()),
]