# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class CsInfo(models.Model):
    scode = models.IntegerField(db_column='sCode', blank=True, null=True)  # Field name made lowercase.
    cat = models.CharField(db_column='Cat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    did = models.CharField(db_column='DID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tid = models.CharField(db_column='TID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ucid = models.CharField(db_column='UCID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phase = models.CharField(db_column='Phase', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='Sname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=255, blank=True, null=True)
    schoolstatus = models.CharField(db_column='SchoolStatus', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cs_info'


class Cst042024(models.Model):
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tehsil = models.CharField(db_column='Tehsil', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schoolcode = models.FloatField(db_column='SchoolCode', blank=True, null=True)  # Field name made lowercase.
    school = models.ForeignKey(CsInfo, on_delete=models.CASCADE)  # Define foreign key
    uniqueid = models.CharField(db_column='UniqueID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    expirydate = models.CharField(db_column='Expirydate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    beneficiaryname = models.CharField(db_column='BeneficiaryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accountno = models.CharField(db_column='AccountNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bankcode = models.FloatField(db_column='BankCode', blank=True, null=True)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    branchcode = models.CharField(db_column='BranchCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    teachercontactno = models.CharField(db_column='TeacherContactno', max_length=255, blank=True, null=True)  # Field name made lowercase.
    father_husband_name = models.CharField(db_column='Father/Husband name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    aidfin = models.CharField(db_column='AIDFin', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=255, blank=True, null=True)  # Field name made lowercase.
    profq = models.CharField(db_column='ProfQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_establishment = models.CharField(db_column='Date of Establishment', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    appoint_date = models.DateTimeField(db_column='Appoint Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_birth = models.CharField(db_column='Date of Birth', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_against_booking = models.CharField(db_column='Payment against booking', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adj_salary_of_july_dec_23 = models.FloatField(db_column='Adj salary of July & Dec 23', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    arrears_deduction = models.FloatField(db_column='Arrears /Deduction', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    non_salary_cost = models.FloatField(db_column='Non-Salary Cost', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    april_2024_salay = models.FloatField(db_column='April  2024 Salay', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_arreas = models.FloatField(db_column='Total Amount with Arreas  for the month of April 2024', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    salary_march_2023 = models.FloatField(db_column='Salary March 2023', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    variance = models.FloatField(db_column='Variance', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cst_04_2024'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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
    id = models.BigAutoField(primary_key=True)
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
