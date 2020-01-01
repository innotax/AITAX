from django import forms
from .models import CtaIdPw

class CtaIdPwForm(forms.ModelForm):
    class Meta:
        model = CtaIdPw
        # fields = '__all__'
        fields = ['agentId', 'agentPw', 'userId', 'userPw']
        labels = model.verbose_name
