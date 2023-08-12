from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=50, choices=[
        ('option1', 'Aplication 1'),
        ('option2', 'Application 2'),
        ('option3', 'Application 3'),
    ])
    text_field = models.CharField(max_length=200)
    file_field = models.FileField(upload_to='application_files/')
    submission_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 100)

    def __str__(self):
        return f"Application by {self.user.username}"

