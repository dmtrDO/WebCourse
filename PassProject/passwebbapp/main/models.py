from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet


class Roles(models.Model):
    roleName = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.roleName}"

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"


class Users(models.Model):
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, password):
        return check_password(password, self.password)

    def __str__(self):
        return f"User with email {self.email}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Settings(models.Model):
    length = models.IntegerField()
    isNumbers = models.BooleanField()
    isLetters = models.BooleanField()
    isSpecial = models.BooleanField()

    def __str__(self):
        return (f"Довжина: {self.length}, Цифри: {self.isNumbers}"
                f", спеціальні символи: {self.isSpecial}, літери: {self.isLetters}")

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"


class GeneratedPasswords(models.Model):
    password = models.CharField(max_length=255)
    association = models.CharField(max_length=255)
    settings = models.ForeignKey(Settings, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.password}"

    def set_password(self, password):
        f = Fernet(settings.FERNET_KEY)
        self.password = f.encrypt(password.encode()).decode()

    def get_password(self):
        f = Fernet(settings.FERNET_KEY)
        return f.decrypt(self.password.encode()).decode()

    class Meta:
        verbose_name = "GeneratedPassword"
        verbose_name_plural = "GeneratedPasswords"




