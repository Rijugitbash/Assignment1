from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    select_application_type = models.CharField(max_length=50, choices=[
        ('application type 1', 'application type 1'),
        ('application type 2', 'application type 2'),
        ('application type 3', 'application type 3'),
    ])
    service_details = models.CharField(max_length=200)
    attach_file = models.FileField(upload_to='application_files/')
    submission_datetime = models.CharField(max_length=100)
    status = models.CharField(max_length = 100)

    def __str__(self):
        return f"Application by {self.user.username}"

