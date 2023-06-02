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
    source_addr = models.CharField(max_length=10, choices=SOURCE_ADDRESS)
    sms_text = models.CharField()
    tel_number_list = ArrayField(models.CharField(max_length=12, validators=[only_int]))
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    sent_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "SMS log"
        verbose_name_plural = "SMS logs"
    
TYPE = (

)
LEVEL = (

)
CATEGORY = (

)
RESPONSIBLE_AREA = (

)
CATEGORY_FOR_HUB = (

)
CATEGORY_FOR_CORE = (

)

EFFECT = (

)

class AlarmReport(models.Model):
    type = models.CharField(max_length=30, choices=TYPE)
    level = models.CharField(max_length=30, choices=LEVEL)
    category = models.CharField(max_length=30, choices=CATEGORY)
    responsible_area = models.CharField(max_length=30, choices=RESPONSIBLE_AREA)
    category_for_hub = models.CharField(max_length=30, choices=CATEGORY_FOR_HUB, )
    category_for_core = models.CharField(max_length=30, choices=CATEGORY_FOR_CORE)
    hub_site = models.CharField(max_length=30, default=None, null=True, blank=True)
    fg_avb = models.CharField(max_length=2, default=None, null=True, blank=True)
    mw_link = models.CharField(max_length=30, default=None, null=True, blank=True)
    mw_equipment = models.CharField(max_length=30, default=None, null=True, blank=True)
    mw_vendor = models.CharField(max_length=30, default=None, null=True, blank=True)
    bts_vendor = models.CharField(max_length=30, default=None, null=True, blank=True)
    power_off_time = models.DateTimeField(default=None, null=True, blank=True)
    sector_block_time = models.DateTimeField(default=None, null=True, blank=True)
    low_battery_time = models.DateTimeField(default=None, null=True, blank=True)
    dg_start_time = models.DateTimeField(default=None, null=True, blank=True)
    battery_life_time = models.TimeField(default=None, null=True, blank=True)
    chronic_site = models.CharField(max_length=30, default=None, null=True, blank=True)
    chronic_hours = models.IntegerField(default=None, null=True, blank=True)
    problem = models.CharField()
    reason = models.CharField()
    influence = models.CharField()
    effect = models.CharField(max_length=30, choices=EFFECT)
    informed = models.CharField(max_length=100, default=None, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(default=None, null=True, blank=True)
    duration = models.DurationField(default=None, null=True, blank=True)
    effect_level = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    description = models.CharField()
    year = models.IntegerField()
    month = models.IntegerField()
    week = models.IntegerField()
    year_week = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
