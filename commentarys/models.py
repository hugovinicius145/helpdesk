from django.db import models
from tickets.models import TbTicket
from status.models import TbStatus

class TbCommentary(models.Model):
    ticket = models.ForeignKey('tickets.TbTicket', models.DO_NOTHING, blank=True, null=True)
    commentary = models.TextField(blank=True, null=True)
    status = models.ForeignKey('status.TbStatus', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_commentary'
