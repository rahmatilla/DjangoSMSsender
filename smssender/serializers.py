from rest_framework import serializers
from .models import SMSReceiver, SMSlog

class SMSReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSReceiver
        fields = ('id', 'network', 'criteria', 'notification', 'tel_number', 'name')

class SMSlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSlog
        fields = ('id', 'source_addr', 'sms_text', 'tel_number_list', 'user', 'sent_time')