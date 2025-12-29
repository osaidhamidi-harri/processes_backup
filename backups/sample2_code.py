
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Books(models.Model):
    sn = models.AutoField(db_column='SN', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(max_length=100)
    pword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'

