from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from .models import SMSReceiver, SMSlog
from .serializers import SMSReceiverSerializer, SMSlogSerializer, SMSSendSerializer
from .local_functions import send_sms_to_many

class SMSReceiverView(generics.ListCreateAPIView):
    queryset = SMSReceiver.objects.all()
    serializer_class = SMSReceiverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'network': ["exact"],
        'criteria': ["in", "exact"], # note the 'in' field
        'notification': ["exact"]
    }
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SMSReceiverRetrive(generics.RetrieveUpdateDestroyAPIView):
    queryset = SMSReceiver.objects.all()
    serializer_class = SMSReceiverSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SMSlogView(generics.ListAPIView):
    queryset = SMSlog.objects.all()
    serializer_class = SMSlogSerializer

class SendSMS(GenericAPIView):
    serializer_class = SMSlogSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        data = {
            'source_addr': data['source_addr'],
            'sms_text': data['sms_text'],
            'tel_number_list': list(dict.fromkeys(data['tel_number_list'])),
            'user': user.id
        }
        serializer = SMSlogSerializer(data=data)
        if serializer.is_valid():
            try:
                send_sms_to_many(src=data['source_addr'].upper(), dest_list=data['tel_number_list'], message=data['sms_text'])
            except Exception as e: print(e)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SMSSend(GenericAPIView):
    serializer_class = SMSSendSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = SMSSendSerializer(data=data)
        if serializer.is_valid():
            tel_number_list = SMSReceiver.objects.filter(
                network=data['network'], criteria__in=data['criteria'], 
                notification=data['notification']).values_list('tel_number', flat=True)
            if len(tel_number_list) > 0:
                try:
                    send_sms_to_many(src=data['source_addr'].upper(), dest_list=tel_number_list, message=data['sms_text'])
                except Exception as e: print(e)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                Response({'status': status.HTTP_404_NOT_FOUND,
                          'detail': "Receivers with these criterias aren't found"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


