from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, password=None):
        """
        Creates and saves a User with the given email, first name, lastname and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        firstname=firstname,
        lastname=lastname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname=None, lastname=None, password=None):
        """
        Creates and saves a User with the given email, first name, lastname and password.
        """
        user = self.create_user(
            email,
            password=password,
            firstname=firstname,
            lastname=lastname,
            )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="آدرس ایمیل",
        max_length=255,
        unique=True,
    )
    firstname = models.CharField(max_length=50, verbose_name= 'نام', null=True, blank=True)
    lastname = models.CharField(max_length=50, verbose_name= 'نام خانوادگی', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name= 'فعال')
    is_admin = models.BooleanField(default=False, verbose_name= 'ادمین')

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin