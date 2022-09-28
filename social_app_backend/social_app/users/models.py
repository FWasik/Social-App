from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name: str, last_name: str, email: str, password: str, middle_name: str, is_staff=False,
                    is_superuser=False) -> "CustomUser":

        if not email:
            raise ValueError("User must have proper email")
        if not first_name:
            raise ValueError("User must have first name")
        if not last_name:
            raise ValueError("User must have last name")
        if not password:
            raise ValueError("User must have password")

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.middle_name = middle_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser

        user.save()

        return user

    def create_superuser(self, first_name: str, last_name: str, email: str, password: str, middle_name="") \
            -> "CustomUser":

        user = self.create_user(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )

        user.save()

        return user


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(verbose_name="First name", max_length=100)
    middle_name = models.CharField(verbose_name="Middle name", max_length=250, blank=True, default="")
    last_name = models.CharField(verbose_name="Last name", max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=250, unique=True)
    password = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]
