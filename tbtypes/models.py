from django.db import models

class TbType(models.Model):
    name_type = models.CharField(max_length=99, blank=True, null=True)
    desc_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_type'