from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    organizer = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    location = models.CharField(max_length=120)
    date = models.DateField()
    time = models.TimeField()
    number_of_seats = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


#new model for when user book an event
class BookEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=70)
    phone_number = models.PositiveIntegerField()
    book_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.event
