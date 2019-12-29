from django.shortcuts import render
from django.conf import settings
from utils import ift
import json
from nts.models import CtaCert
from django.db import IntegrityError
from django.contrib import messages  # 경고창 https://hoy.kr/kxuTa

# Create your views here.

def cert_info(request):
    print(settings.BASE_DIR)
    return render(request, 'cert_info.html')

def output(request):
    data = ift.cert_info()
    dic = json.loads(data)
    if dic['cert_nm'] == "":
        msg = "공인인증서 선택 및 비밀번호 입력후 확인버튼을 누르세요!!!"
        messages.add_message(request, messages.INFO, msg)
        return render(request, 'cert_info.html')
    try:
        ctacert = CtaCert(**dic)  # 인스턴스
        ctacert.save()
    except IntegrityError as e:
        msg = "이미 저장된 공인인증서 입니다!!!"
        messages.add_message(request, messages.INFO, msg)
        return render(request, 'cert_info.html')
        
    return render(request, 'cert_info.html', {'dic':dic})
