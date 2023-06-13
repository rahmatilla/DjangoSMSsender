from rest_framework import serializers
from .models import SMSReceiver, SMSlog, AlarmReport, CRITERIA_CHOISE, NOTIFICATION_CHOISE, NETWORK_CHOISE, SOURCE_ADDRESS
class SMSReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSReceiver
        fields = ('id', 'network', 'criteria', 'notification', 'tel_number', 'name')

class SMSlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSlog
        fields = ('id', 'source_addr', 'sms_text', 'tel_number_list', 'user', 'sent_time')

class AlarmReportSerializers(serializers.ModelSerializer):

    class Meta:
        model = AlarmReport
        fields = '__all__'

class SMSSendSerializer(serializers.Serializer):
    source_addr = serializers.ChoiceField(choices=SOURCE_ADDRESS)
    network = serializers.ChoiceField(choices=NETWORK_CHOISE)
    criteria = serializers.MultipleChoiceField(choices=CRITERIA_CHOISE)
    notification = serializers.ChoiceField(choices=NOTIFICATION_CHOISE)
    sms_text = serializers.CharField()