from django.contrib.auth.models import AbstractUser


class Murren(AbstractUser):

    def __str__(self):
        return self.username
