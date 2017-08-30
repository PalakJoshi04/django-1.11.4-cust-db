from django.db import models
from .validators import *


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, validators=[validate_first_name])
    last_name = models.CharField(max_length=20, validators=[validate_last_name])

    def __unicode__(self):
        return "{0} {1}".format(self.first_name, self.last_name)