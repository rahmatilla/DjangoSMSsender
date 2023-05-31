from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


def only_int(value): 
    if value.isdigit()==False:
        raise ValidationError('Phone number contains characters')

NETWORK_CHOISE = (
    ("cn", 'CN'),
    ("rn", 'RN')
)
# NETWORK_CHOISE = ('CN', 'RN')
CRITERIA_CHOISE = (
    ("a2", 'A2'),
    ("a3", 'A3'),
    ("a4", 'A4'),
    ("a5", 'A5'),
    ("an", 'Andijan'),
    ("bh", 'Bukhara'),
    ("dz", 'Djizzakh'),
    ("fr", 'Fergana'),
    ("sr", 'Sirdarya'),
    ("ks", 'Kashkadarya'),
    ("nm", 'Namangan'),
    ("nv", 'Navoi'),
    ('kr', 'Karakalpakstan'),
    ("sm", 'Samarkand'),
    ("ts", 'Tashkent'),
    ("su", 'Surkhandarya'),
    ("kh", 'Khorezm'),
)

NOTIFICATION_CHOISE = (
    ("internet", 'Internet Incidents'),
    ("roaming", 'Roaming Incidents'),
    ("core", 'Core Incidents'),
    ("power", 'Power Incidents'),
    ("controller", 'BSC/RNC Incidents'),
    ("chronic", 'Chronic-Down Sites'),
    ("hub", 'HUB Sites Incidents'),
    ("report", 'Report Message'),
)

SOURCE_ADDRESS = (
    ('ncc-rn', 'NCC-RN'),
    ('ncc-cn', 'NCC-CN'),
    ('uzavtosavdo', 'UzAvtoSavdo')
)

class SMSReceiver(models.Model):
    network = models.CharField(max_length=10, choices=NETWORK_CHOISE)
    criteria = models.CharField(max_length=20, choices=CRITERIA_CHOISE)
    notification = models.CharField(max_length=30, choices=NOTIFICATION_CHOISE)
    tel_number = models.CharField(max_length=12, validators=[only_int])
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "SMS receiver"
        verbose_name_plural = "SMS receivers"

class SMSlog(models.Model):
    source_addr = models.CharField(max_length=12, choices=SOURCE_ADDRESS)
    sms_text = models.CharField()
    tel_number_list = ArrayField(models.CharField(max_length=12, validators=[only_int]))
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    sent_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "SMS log"
        verbose_name_plural = "SMS logs"
    
 
