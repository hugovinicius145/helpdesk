from django.db import models

class TbLevel(models.Model):
    name_level = models.CharField(max_length=99, blank=True, null=True)
    desc_level = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_level'