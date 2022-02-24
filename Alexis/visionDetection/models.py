from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .manager import UserManager
from django.utils.translation import gettext_lazy


def authenticate(email: str, password: str):
    user = User.objects.get(email=email)
    if user is None:
        return None
    if user is not None:
        if user.check_password(password):
            if user.is_active:
                return user
            else:
                return "User is not activated"
    return None


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    country = models.CharField(max_length=25, null=False, )
    phone_no = models.CharField(max_length=12, null=False, )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    PASSWORD_FIELD = 'password'
    REQUIRED_FIELDS = ['country', 'name', 'phone_no', 'password']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % self.pk

