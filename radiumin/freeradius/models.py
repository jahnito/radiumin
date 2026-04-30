from django.db import models


class FixedCharField(models.CharField):
    description = "Fixed-length char field"

    def db_type(self, connection):
        # Переопределяем метод, чтобы явно вернуть CHAR(N)
        return f'CHAR({self.max_length})'


class NasModel(models.Model):
    nasname = models.CharField(max_length=128, null=False)
    shortname = models.CharField(max_length=32)
    type_nas = models.CharField(
        max_length=30, db_column='type', default='other'
    )
    ports = models.IntegerField()
    secret = models.CharField(max_length=60, null=False, default='secret')
    server = models.CharField(max_length=64)
    community = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default='RADIUS Client')

    class Meta:
        managed = False
        db_table = 'nas'


class NasreloadModel(models.Model):
    nasipaddress = models.CharField(
        max_length=15, null=False, primary_key=True
    )
    reloadtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nasreload'


class RadacctModel(models.Model):
    radacctid = models.BigIntegerField(
        primary_key=True, null=False
    )
    acctsessionid = models.CharField(max_length=64, null=False, default='')
    acctuniqueid = models.CharField(max_length=32, null=False, default='')
    rad_username = models.CharField(
        max_length=64, db_column='username', null=False, default=''
    )
    realm = models.CharField(max_length=64, default='')
    nasipaddress = models.CharField(max_length=15, null=False, default='')
    nasportid = models.CharField(max_length=32, default=None)
    nasporttype = models.CharField(max_length=32, default=None)
    acctstarttime = models.DateTimeField(default=None)
    acctupdatetime = models.DateTimeField(default=None)
    acctstoptime = models.DateTimeField(default=None)
    acctinterval = models.IntegerField(default=None)
    acctsessiontime = models.IntegerField(default=None)
    acctauthentic = models.CharField(max_length=32, default=None)
    connectinfo_start = models.CharField(max_length=128, default=None)
    connectinfo_stop = models.CharField(max_length=128, default=None)
    acctinputoctets = models.BigIntegerField(default=None)
    acctoutputoctets = models.BigIntegerField(default=None)
    calledstationid = models.CharField(max_length=50, null=False, default='')
    callingstationid = models.CharField(max_length=50, null=False, default='')
    acctterminatecause = models.CharField(max_length=32, null=False, default='')
    servicetype = models.CharField(max_length=32, default=None)
    framedprotocol = models.CharField(max_length=32, default=None)
    framedipaddress = models.CharField(max_length=15, null=False, default='')
    framedipv6address = models.CharField(max_length=45, null=False, default='')
    framedipv6prefix = models.CharField(max_length=45, null=False, default='')
    framedinterfaceid = models.CharField(max_length=44, null=False, default='')
    delegatedipv6prefix = models.CharField(max_length=45, null=False, default='')
    rad_class = models.CharField(max_length=64, db_column='class', default=None)

    class Meta:
        managed = False
        db_table = 'radacct'


class RadcheckModel(models.Model):
    rad_username = models.CharField(
        max_length=64, null=False, default='', db_column='username'
    )
    attribute = models.CharField(max_length=64, null=False, default='')
    op = FixedCharField(max_length=2, null=False, default='==')
    value = models.CharField(max_length=253, null=False, default='')

    class Meta:
        managed = False
        db_table = 'radcheck'


class RadgroupcheckModel(models.Model):
    groupname = models.CharField(max_length=64, null=False, default='')
    attribute = models.CharField(max_length=64, null=False, default='')
    op = FixedCharField(max_length=2, null=False, default='==')
    value = models.CharField(max_length=253, null=False, default='')

    class Meta:
        managed = False
        db_table = 'radgroupcheck'


class RadgroupreplyModel(models.Model):
    groupname = models.CharField(max_length=64, null=False, default='')
    attribute = models.CharField(max_length=64, null=False, default='')
    op = FixedCharField(max_length=2, null=False, default='=')
    value = models.CharField(max_length=253, null=False, default='')

    class Meta:
        managed = False
        db_table = 'radgroupreply'


class RadpostauthModel(models.Model):
    rad_username = models.CharField(
        max_length=64, null=False, default='', db_column='username'
    )
    rad_pass = models.CharField(
        max_length=64, null=False, default='', db_column='pass'
    )
    reply = models.CharField(max_length=64, null=False, default='')
    authdate = models.DateTimeField(null=False, auto_now_add=True)
    rad_class = models.CharField(
        max_length=64, default=None, db_column='class')

    class Meta:
        managed = False
        db_table = 'radpostauth'


class RadreplyModel(models.Model):
    rad_username = models.CharField(
        max_length=64, null=False, default='', db_column='username'
    )
    attribute = models.CharField(max_length=64, null=False, default='')
    op = FixedCharField(max_length=2, null=False, default='=')
    value = models.CharField(max_length=253, null=False, default='')

    class Meta:
        managed = False
        db_table = 'radreply'


class RadusergroupModel(models.Model):
    rad_username = models.CharField(
        max_length=64, null=False, default='', db_column='username'
    )
    groupname = models.CharField(max_length=64, null=False, default='')
    priority = models.IntegerField(null=False, default=1)

    class Meta:
        managed = False
        db_table = 'radusergroup'
