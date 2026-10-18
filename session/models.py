from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

import uuid


class CustomUserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("You must provide an unique username")

        if not email:
            raise ValueError("You must provide an unique email address")

        email = self.normalize_email(email)

        user = self.model(username = username, **extra_fields)

        user.set_password(password)

        user.save(using = self._db)

        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser" , False)

        extra_fields.setdefault("is_staff" , False)

        extra_fields.setdefault("is_active" , False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username = None, email = None, password = None, **extra_fields):
        
        extra_fields.setdefault("is_superuser" , True)
        
        extra_fields.setdefault("is_staff" , True)
        
        extra_fields.setdefault("is_active" , True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser == True")

        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active == True")

        return self._create_user(username, email, password , **extra_fields)
            


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)

    first_name = models.CharField(max_length = 50)

    last_name = models.CharField(max_length = 50)

    username = models.CharField(max_length = 50, unique = True)

    email = models.EmailField(unique = True)

    image = models.ImageField(upload_to = "user_images/", blank = True , null = True)

    class UserTypeChoices(models.TextChoices):

        ADMIN = "admin" , "Admin"

        EDITOR = "editor" , "Editor"

        READER = "reader" , "Reader"

        AUTHOR = "author" , "Author"

        ADVERTISER = "advertiser" , "Advertiser"


    user_type = models.CharField(max_length = 12, default = UserTypeChoices.READER, choices = UserTypeChoices.choices)

    class GenderChoices(models.TextChoices):

        MALE = "male" , "Male"

        FEMALE = "female" , "Female"

        THIRD = "third" , "Third"

        TRANS = "transgender" , "Transgender"

    gender = models.CharField(max_length = 12, default = GenderChoices.MALE, choices = GenderChoices.choices)

    date_of_birth = models.DateField(blank = True , null = True)

    is_active = models.BooleanField(default = False)

    is_staff = models.BooleanField(default = False)

    joined_at = models.DateTimeField(auto_now_add = True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["email"]

    class Meta:
        ordering = ["-joined_at"]

        verbose_name = "User"

        verbose_name_plural = "Users"