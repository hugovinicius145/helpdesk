from django.db import models

class TbCategory(models.Model):
    name_category = models.CharField(max_length=99, blank=True, null=True)
    desc_category = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_category'

    def __str__(self):
        return self.name_category