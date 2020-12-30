from django.db import models


# Create your models here.

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=True, default='SN')
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'tbl_endereco'
        managed = True
        verbose_name = "Endereco"
        verbose_name_plural = "Enderecos"


class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'tbl_curso'
        managed = True
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        abstract = True


class Profissional(Pessoa):
    formacao = models.ManyToManyField('Curso', db_table='tbl_pessoa_curso')
    habilidades = models.TextField(blank=True, null=True)
    experiencia = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'tbl_profissional'
        managed = True
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'


class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    profissional = models.ForeignKey('Profissional', null=False, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_perfil'
        managed = True
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
