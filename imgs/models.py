from django.db import models
from tickets.models import TbTicket

class TbImg(models.Model):
    ticket = models.ForeignKey('tickets.TbTicket', models.DO_NOTHING, blank=True, null=True)
    img = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_img'