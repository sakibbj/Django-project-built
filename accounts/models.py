from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, firstName, lastName, userName, email, password=None):
        if not email:
            raise ValueError('User Must Have an Email address')
        
        if not userName:
            raise ValueError('User Must Have an Username')
        
        user = self.model(
            email = self.normalize_email(email),
            userName = userName,
            firstName = firstName,
            lastName = lastName, 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, firstName, lastName, email, userName, password):
        user = self.create_user(
            email = self.normalize_email(email),
            userName = userName,
            password =  password,
            firstName = firstName,
            lastName = lastName,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=50)

    #required fields
    date_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)
    is_suparadmin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userName', 'firstName', 'lastName']

    objects = AccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
