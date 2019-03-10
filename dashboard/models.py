from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.username, filename)

class Uploaddata(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    upload = models.FileField(default='SIH.csv', upload_to=user_directory_path)

    def __str__(self):
        return f'{self.user.username} dataset'

class War(models.Model):
    war_id  = models.IntegerField()
    war_name = models.CharField(max_length=100) 
    war_type = models.IntegerField()
    side1_code = models.IntegerField()
    side1_name = models.CharField(max_length=100)
    side2_code = models.IntegerField()
    side2_name = models.IntegerField()
    start_year1 = models.IntegerField()
    start_month1 = models.IntegerField()
    start_day1 = models.IntegerField()
    end_year1 = models.IntegerField()
    end_month1 = models.IntegerField()
    end_day1 = models.IntegerField()
    start_year2 = models.IntegerField()
    start_month2 = models.IntegerField()
    start_day2 = models.IntegerField()
    end_year2 = models.IntegerField()
    end_month2 = models.IntegerField()
    end_day2 = models.IntegerField()
    previous_war = models.IntegerField()
    initiation = models.IntegerField()
    intervention = models.IntegerField()
    combat_location = models.IntegerField()
    state_fatalities = models.IntegerField()
    nonstate_fatalities = models.IntegerField()
    outcome = models.IntegerField()
    next_war = models.IntegerField()
