from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def create_user(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.save()

class Notes(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=200)



