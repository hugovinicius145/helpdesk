from django.db import models
from tbtypes.models import TbType
from levels.models import TbLevel
from category.models import TbCategory
from locations.models import TbLocation
from status.models import TbStatus

class TbTicket(models.Model):
    type = models.ForeignKey('tbtypes.TbType', models.DO_NOTHING, blank=True, null=True)
    level = models.ForeignKey('levels.TbLevel', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('category.TbCategory', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('locations.TbLocation', models.DO_NOTHING, blank=True, null=True)
    name_requester = models.CharField(max_length=99, blank=True, null=True)
    machine_name = models.CharField(max_length=99, blank=True, null=True)
    anydesk_number = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=45, blank=True, null=True)
    status = models.ForeignKey('status.TbStatus', models.DO_NOTHING, blank=True, null=True)
    open_date = models.CharField(max_length=99, blank=True, null=True)
    attached_img = models.CharField(max_length=10, blank=True, null=True)
    open_hour = models.CharField(max_length=20, blank=True, null=True)

    class Meta:# Create your models here.
        managed = True
        db_table = 'tb_ticket'
