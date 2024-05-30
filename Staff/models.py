from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name


class Jobs(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'jobs'

    def __str__(self):
        return self.name


class Workers(models.Model):
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(max_length=64, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=17, blank=True, null=True)
    image = models.ImageField(upload_to='profile_image/', default='default_image.png')
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} - {self.job.name} - {self.company.name}'
