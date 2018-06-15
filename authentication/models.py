from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Account( AbstractBaseUser ):
    email = models.EmailField( unique = True )
    username = models.CharField( max_length = 40, unique = True )

    first_name = models.CharField( max_length = 40, blank = True )
    last_name = models.CharField( max_length = 40, blank = True )
    tagline = models.CharField( max_length = 140, blank = True )

    is_admin = models.BooleanField( default = False )

    