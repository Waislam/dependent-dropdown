from django.db import models

# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='districts')
    def __str__(self):
        return self.name

class Thana(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='thanas')
    def __str__(self):
        return self.name

class PostOffice(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='postoffices')
    def __str__(self):
        return self.name

class PostCode(models.Model):
    name = models.CharField(max_length=100)
    # district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='postcodes')
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE, related_name='postcodess', null=True)
    def __str__(self):
        return self.name




class Location(models.Model):
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True, related_name='divisions')
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True, related_name='districts')
    thana = models.ForeignKey(Thana, on_delete=models.SET_NULL, blank=True, null=True, related_name='thanas')
    post_office = models.ForeignKey(PostOffice, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_offices')
    post_code = models.ForeignKey(PostCode, on_delete=models.SET_NULL, blank=True, null=True, related_name='post_cods')

