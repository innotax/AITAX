from django.contrib import admin
from .models import CtaCert, CtaIdPw

# Register your models here.
# addmin.site.register(CtaCert)
@admin.register(CtaCert)
class CtaCertAdmin(admin.ModelAdmin):
    list_display = ('cert_nm', 'end_dt')


admin.site.register(CtaIdPw)
