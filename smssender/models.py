from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import datetime


def only_int(value): 
    if value.isdigit()==False:
        raise ValidationError('Phone number contains characters')

NETWORK_CHOISE = (
    ("CN", 'CN'),
    ("RN", 'RN')
)
# NETWORK_CHOISE = ('CN', 'RN')
CRITERIA_CHOISE = (
    ("A2", 'A2'),
    ("A3", 'A3'),
    ("A4", 'A4'),
    ("A5", 'A5'),
    ("Andijan", 'Andijan'),
    ("Bukhara", 'Bukhara'),
    ("Djizzakh", 'Djizzakh'),
    ("Fergana", 'Fergana'),
    ("Sirdarya", 'Sirdarya'),
    ("Kashkadarya", 'Kashkadarya'),
    ("Namangan", 'Namangan'),
    ("Navoi", 'Navoi'),
    ('Karakalpakstan', 'Karakalpakstan'),
    ("Samarkand", 'Samarkand'),
    ("Tashkent", 'Tashkent'),
    ("Surkhandarya", 'Surkhandarya'),
    ("Khorezm", 'Khorezm'),
)

NOTIFICATION_CHOISE = (
    ("Internet", 'Internet Incidents'),
    ("Roaming", 'Roaming Incidents'),
    ("Core", 'Core Incidents'),
    ("Power/HighTemp", 'Power/HighTemp Incidents'),
    ("BSC/RNC", 'BSC/RNC Incidents'),
    ("Chronic", 'Chronic-Down Sites'),
    ("Hub", 'HUB Sites Incidents'),
    ("Report", 'Report Message'),
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
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT, editable=False)
    sent_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "SMS log"
        verbose_name_plural = "SMS logs"
    
TYPE = (
    ("BSC/RNC", 'BSC/RNC'),
    ("HUB", 'HUB'),
    ("CHRONIC", 'CHRONIC'),
    ("CORE", 'CORE'),

)
LEVEL = (
    ("A1", 'A1'),
    ("A2", 'A2'),
    ("A3", 'A3'),
    ("A4", 'A4'),
    ("A5", 'A5'),
    ("ПР", 'ПР')

)
CATEGORY = (
    ("Тех проблема", "Тех проблема"),
    ("ЭС и Клим", 'ЭС и Клим'),
    ("ПР", 'ПР'),
    ("Выясняется", 'Выясняется')

)
RESPONSIBLE_AREA = (
    ("Другие ЗО", "Другие ЗО"),
    ("Эксплуатация", 'Эксплуатация'),
    ("Выясняется", 'Выясняется')

)
CATEGORY_FOR_HUB = (
    ("AC/DC breaker", "AC/DC breaker"),
    ("Bad RX level", "Bad RX level"),
    ("High Temp", "High Temp"),
    ("Incorrect work", "Incorrect work"),
    ("Leased Line", "Leased Line"),
    ("Low voltage", "Low voltage"),
    ("Power", "Power"),
    ("TI_DNO", "TI_DNO"),
    ("TI_ESO", "TI_ESO"),
    ("TI_MW", "TI_MW"),
    ("TI_SAQ", "TI_SAQ"),
    ("TI_SDH", "TI_SDH"),
    ("Unplanned work", "Unplanned work"),
    ("WB", "WB"),
    ("Выясняется", "Выясняется"),

)
CATEGORY_FOR_CORE = (
    ("Core", "Core"),
    ("GPRS", "GPRS"),
    ("Roaming", "Roaming"),
    ("MPLS", "MPLS"),
    ("Power", "Power"),
    ("High Temp", "High Temp")

)

EFFECT = (
    ("С влиянием", "С влиянием"),
    ("Без влияния", "Без влияния")

)

class AlarmReport(models.Model):
    type = models.CharField(max_length=30, choices=TYPE, verbose_name="Тип")
    level = models.CharField(max_length=30, choices=LEVEL, verbose_name="Уровень")
    category = models.CharField(max_length=30, choices=CATEGORY, verbose_name="Категория")
    responsible_area = models.CharField(max_length=30, choices=RESPONSIBLE_AREA, verbose_name="Зона ответственности")
    category_for_hub = models.CharField(max_length=30, choices=CATEGORY_FOR_HUB, default=None, null=True, blank=True, verbose_name="Категория для БС")
    category_for_core = models.CharField(max_length=30, choices=CATEGORY_FOR_CORE, default=None, null=True, blank=True, verbose_name="Категория для Core")
    hub_site = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name="Хаб сайт")
    fg_avb = models.CharField(max_length=2, default=None, null=True, blank=True, verbose_name="Наличие FG")
    mw_link = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name="MW линк")
    mw_equipment = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name="МW оборудование")
    mw_vendor = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name="MW вендор")
    bts_vendor = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name="BTS вендор")
    power_off_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name="Время отключения питания")
    sector_block_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name="Время блока сектора")
    low_battery_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name="Время низкого заряда батареи")
    dg_start_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name="Время начала DG")
    battery_life_time = models.TimeField(default=None, null=True, blank=True, verbose_name="Battery life time")
    chronic_site = models.CharField(max_length=30, default=None, null=True, blank=True, verbose_name="Хроник сайт")
    chronic_hours = models.IntegerField(default=None, null=True, blank=True, verbose_name="Хроник часы")
    problem = models.CharField(verbose_name="Проблема")
    reason = models.CharField(verbose_name="Причина")
    influence = models.CharField(max_length=100, default=None, null=True, blank=True, verbose_name="Влияние")
    effect = models.CharField(max_length=30, choices=EFFECT, verbose_name="Эффект")
    informed = models.CharField(max_length=100, default=None, null=True, blank=True, verbose_name="Информирован")
    start_time = models.DateTimeField(verbose_name="Начало")
    end_time = models.DateTimeField(default=None, null=True, blank=True, verbose_name="Конец")
    duration = models.DurationField(default=None, null=True, blank=True, verbose_name="Длительность", editable=False)
    region = models.CharField(max_length=30, verbose_name="Регион")
    description = models.CharField(default=None, null=True, blank=True, verbose_name="Описание")
    year = models.IntegerField(verbose_name="Год", editable=False)
    month = models.IntegerField(verbose_name="Месяц", editable=False)
    week = models.IntegerField(verbose_name="Неделя", editable=False)
    year_week = models.CharField(max_length=30, verbose_name="Неделя+Год", editable=False)
    effect_level = models.CharField(max_length=30, verbose_name="Уровень + Эффект", editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан в")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено в")
    is_complete = models.BooleanField(default=False, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)

    def save(self, *args, **kwargs):
        if self.end_time:
            self.duration = self.end_time - self.start_time
            self.is_complete = True
        self.year = self.start_time.year
        self.month = self.start_time.month
        self.week =  datetime.date(self.start_time.year, self.start_time.month, self.start_time.day).isocalendar()[1]
        self.year_week = str(self.year) + '_' + str(self.week)
        self.effect_level = self.effect + ' ' + self.level
        super(AlarmReport, self).save(*args, **kwargs)
