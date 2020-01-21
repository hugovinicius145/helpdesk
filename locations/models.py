from django.db import models

class TbLocation(models.Model):
    name_location = models.CharField(max_length=99, blank=True, null=True)
    initials = models.CharField(max_length=20, blank=True, null=True)
    desc_location = models.CharField(max_length=99, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_location'
