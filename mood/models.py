from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

from mood.choices import *

class Day(models.Model):
	date = models.DateField()
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
        )

	def __str__(self):
		return str(self.date)

class Entry(models.Model):
	description = models.CharField(max_length=200, null=True, blank=True)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
        )

	tod = models.CharField(max_length=1, choices=TIME_OF_DAY_CHOICES)

	day = models.ForeignKey(Day, on_delete=models.CASCADE)

	happiness_level = models.IntegerField(choices=MOOD_RATING_CHOICES, default=0)
	anger_level = models.IntegerField(choices=MOOD_RATING_CHOICES, default=0)
	anxiety_level = models.IntegerField(choices=MOOD_RATING_CHOICES, default=0)
	energy_level = models.IntegerField(choices=MOOD_RATING_CHOICES, default=0)
	motivation_level = models.IntegerField(choices=MOOD_RATING_CHOICES, default=0)

	
	def __str__(self):
		return str(self.get_tod_display())

	def get_absolute_url(self):
		return reverse('entry_edit', kwargs={'pk' : self.pk })


