
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class User(models.Model):
    id_user = models.ForeignKey(AuthUser,models.DO_NOTHING, db_column='id_auth_user', blank=True, null=True)

class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorias(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'categorias'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Encuestas(models.Model):
    idencuesta = models.AutoField(db_column='idEncuesta', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'encuestas'


class Fichas(models.Model):
    idfichas = models.AutoField(db_column='idFichas', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField()
    gad_servi_usuario = models.ForeignKey('GadSerUser', models.DO_NOTHING)
    pregunta_respuesta = models.ForeignKey('PreguntasRespuestas', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fichas'


class Gad(models.Model):
    id_gad = models.AutoField(primary_key=True)
    gad = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'gad'

    def __str__(self):
        return '%s' % (self.gad)

class GadSerUser(models.Model):
    idgadservuser = models.AutoField(db_column='idGadServUser', primary_key=True)  # Field name made lowercase.
    gad_ser = models.ForeignKey('GadsServicios', models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gad_ser_user'


class GadsServicios(models.Model):
    idgadservicio = models.AutoField(db_column='idGadServicio', primary_key=True)  # Field name made lowercase.
    gad = models.ForeignKey(Gad, models.DO_NOTHING)
    servicios = models.ForeignKey('Servicios', models.DO_NOTHING)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'gads_servicios'

    def __str__(self):
        return '%s' % (self.servicios)


class Preguntas(models.Model):
    idpregunta = models.AutoField(db_column='idPregunta', primary_key=True)  # Field name made lowercase.
    pregunta = models.CharField(max_length=300)
    encuesta = models.ForeignKey(Encuestas, models.DO_NOTHING)
    subcategoria = models.ForeignKey('Subcategorias', models.DO_NOTHING, db_column='subCategoria_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preguntas'


class PreguntasRespuestas(models.Model):
    idpreguntaresp = models.AutoField(db_column='idPreguntaResp', primary_key=True)  # Field name made lowercase.
    pregunta = models.ForeignKey(Preguntas, models.DO_NOTHING, blank=True, null=True)
    respuesta = models.ForeignKey('Respuestas', models.DO_NOTHING, blank=True, null=True)
    valor = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preguntas_respuestas'

    def __str__(self):
        return '%s' % (self.respuesta)

class Respuestas(models.Model):
    idrespuesta = models.AutoField(db_column='idRespuesta', primary_key=True)  # Field name made lowercase.
    respuesta = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'respuestas'

    def __str__(self):
        return '%s' % (self.respuesta)


class Servicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    servicio = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'servicios'

    def __str__(self):
        return '%s' % (self.servicio)

class Subcategorias(models.Model):
    id_subcategoria = models.AutoField(primary_key=True)
    subcategoria = models.CharField(max_length=300)
    categoria = models.ForeignKey(Categorias, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'subcategorias'
