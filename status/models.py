from django.db import models

class TbStatus(models.Model):
    name_status = models.CharField(max_length=99, blank=True, null=True)
    description = models.CharField(max_length=99, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_status'
