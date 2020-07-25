# Generated by Django 2.2.6 on 2020-06-20 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('idcategoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'categorias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Encuestas',
            fields=[
                ('idencuesta', models.AutoField(db_column='idEncuesta', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'encuestas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fichas',
            fields=[
                ('idfichas', models.AutoField(db_column='idFichas', primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'fichas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gad',
            fields=[
                ('id_gad', models.AutoField(primary_key=True, serialize=False)),
                ('gad', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'gad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GadSerUser',
            fields=[
                ('idgadservuser', models.AutoField(db_column='idGadServUser', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'gad_ser_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GadsServicios',
            fields=[
                ('idgadservicio', models.AutoField(db_column='idGadServicio', primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'gads_servicios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('idpregunta', models.AutoField(db_column='idPregunta', primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'preguntas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PreguntasRespuestas',
            fields=[
                ('idpreguntaresp', models.AutoField(db_column='idPreguntaResp', primary_key=True, serialize=False)),
                ('valor', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'preguntas_respuestas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('idrespuesta', models.AutoField(db_column='idRespuesta', primary_key=True, serialize=False)),
                ('respuesta', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'respuestas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('servicio', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'servicios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subcategorias',
            fields=[
                ('id_subcategoria', models.AutoField(primary_key=True, serialize=False)),
                ('subcategoria', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'subcategorias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.ForeignKey(blank=True, db_column='id_auth_user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='encuesta.AuthUser')),
            ],
        ),
    ]
