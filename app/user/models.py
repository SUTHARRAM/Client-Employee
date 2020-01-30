from django.db import models

# Create your models here.

class employee(models.Model):
    """ Employee table """
    employee_name = models.CharField(max_length=255, null=True, blank=False)
    employee_id = models.IntegerField(unique=True)

    class Meta:
        default_permissions = {'change', 'add', 'delete', 'view'}

    def __str__(self):
        return self.employee_name

class client(models.Model):
    """ Client Models """
    client_name = models.CharField(max_length=255, null=True, blank=False)
    client_id = models.IntegerField(unique=True)

    class Meta:
        default_permissions = {'view'}

    def __str__(self):
        return self.client_name