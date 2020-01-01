from django.db import models
from django.urls import reverse

# Create your models here.
class CtaCert(models.Model):

    cert_nm = models.CharField(max_length=100, verbose_name='인증서명')
    pub_dt = models.DateField(verbose_name='유효기간시작일')
    end_dt = models.DateField(verbose_name='유효기간종료일')
    org_nm = models.CharField(max_length=20, verbose_name='인증기관')
    oid = models.CharField(max_length=30, verbose_name='인증기관ID')
    sn = models.CharField(max_length=20, verbose_name='시리얼넘버')
    file1 = models.CharField(max_length=1000, verbose_name='인증서')
    file2 = models.CharField(max_length=1000, verbose_name='개인키')
    cert_pw = models.CharField(max_length=20, verbose_name='인증서비번')
    display_default = models.IntegerField(default=0, verbose_name='선택횟수')

    def __str__(self):
        return self.cert_nm
    
    class Meta:
        unique_together = (('cert_nm', 'end_dt'),)

class CtaIdPw(models.Model):
    ctacert = models.ForeignKey(CtaCert, on_delete=models.CASCADE)  # db 의 무결성 CASCADE
    agentId = models.CharField(max_length=30, verbose_name='세무사관리번호')
    agentPw = models.CharField(max_length=30, verbose_name='세무사비밀번호')
    userId = models.CharField(max_length=30, verbose_name='사용자아이디')
    userPw = models.CharField(max_length=30, verbose_name='사용자비밀번호')
    use_cnt = models.IntegerField(default=0, verbose_name='사용횟수')

    def __str__(self):
        return self.userId

    def get_absolute_url(self):
        return reverse("nts", kwargs={"pk": self.pk})
    

    class Meta:
        unique_together = (('userId', 'userPw'),)
