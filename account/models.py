from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__password = self.password

    email = models.EmailField(verbose_name='Email', unique=True)
    is_active = models.BooleanField(verbose_name='Is Active', default=False)
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    phone_number = PhoneNumberField(verbose_name='Phone Number', help_text='e.g: +98 ...')
    password = models.CharField(verbose_name='Password', help_text='Hashed Password', max_length=128)
    REQUIRED_FIELDS = ('first_name', 'last_name')

    class Meta:
        db_table = 'pyfarsi_users'
        ordering = ('-date_joined',)

    def save(self, *args, **kwargs):
        if self.__password != self.password:
            self.set_password(self.password)

    def save(self, *args, **kwargs):
        if self.__password != self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)