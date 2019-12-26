from django.db import models

# Create your models here.
class CtaCert(models.Model):
    cert_nm = models.CharField(max_length=100, verbose_name='인증서명')
    end_dt = models.DateField(verbose_name='유효기간')
    org_nm = models.CharField(max_length=20, verbose_name='인증기관')
    sn = models.CharField(max_length=20, verbose_name='시리얼넘버')
    file1 = models.CharField(max_length=1000, verbose_name='인증서')
    file2 = models.CharField(max_length=1000, verbose_name='개인키')
    cert_pw = models.CharField(max_length=20, verbose_name='인증서비번')
    
