from django.db import models

class TbUseradmin(models.Model):
    userdomainname = models.CharField(unique=True, max_length=99, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=99, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'tb_useradmin'
