import datetime
from django.utils import timezone
from django.db import models


class Week(models.Model):
    pub_date = models.DateTimeField("Date published")
    today = datetime.datetime.today()

    def start_of_week(self):
        return self.today + datetime.timedelta(days=-self.today.weekday(), weeks=1)  # Start of week

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    dessert_choice = models.CharField(max_length=200)
    dessert_details = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.dessert_choice
