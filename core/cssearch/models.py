from django.db import models

# Create your models here.
class csinfo(models.Model):
    scode = models.CharField(max_length=10, unique=True,blank=False)
    id = models.AutoField(primary_key=True)
    # scode = models.IntegerField(db_column='sCode', blank=True, null=True)  # Field name made lowercase.
    cat = models.CharField(db_column='Cat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    did = models.CharField(db_column='DID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tid = models.CharField(db_column='TID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ucid = models.CharField(db_column='UCID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phase = models.CharField(db_column='Phase', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='Sname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=255, blank=True, null=True)
    schoolstatus = models.CharField(db_column='SchoolStatus', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'csinfo'
    def __str__(self): 
        return self.sname 

class cst042024(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tehsil = models.CharField(db_column='Tehsil', max_length=255, blank=True, null=True)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scode = models.CharField(db_column='scode',max_length=10)
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
        # managed = False
        db_table = 'cst042024'

    def __str__(self): 
        return self.schoolname + ' ' +self.beneficiaryname