from django.db import models
from django.contrib.auth.models import User

class SMTPSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    smtp_server = models.CharField(max_length=100)
    smtp_port = models.IntegerField()
    email_host_user = models.EmailField()
    email_host_password = models.CharField(max_length=100)

class SentEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
