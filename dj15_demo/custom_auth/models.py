import re

from django.db import models
from django.contrib.auth import models as auth_models

class CustomUserManager(auth_models.BaseUserManager):
    def create_user(self, email, mobile, password):

        user = self.model(
                            email  = CustomUserManager.normalize_email(email),
                            mobile = mobile,
                         )

        user.is_staff = True
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, mobile, password):
        print "ValueError"
        if not re.match(r'^\d{10}$', mobile):
            raise ValueError('Enter a valid mobile number')

        user = self.model(
                            email  = CustomUserManager.normalize_email(email),
                            mobile = mobile,
                         )

        user.is_staff = True
        user.is_superuser  = True
        user.set_password(password)
        user.save(using = self._db)
        return user

class UserProfile(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email     = models.EmailField(verbose_name = 'E-Mail', unique = True)
    mobile    = models.CharField(verbose_name = 'Mobile Number', max_length = 10, unique = True)
    is_staff  = models.BooleanField()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['mobile', ]
    objects         = CustomUserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def is_staff(self):
        return self.is_staff
