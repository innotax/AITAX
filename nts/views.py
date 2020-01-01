from django.shortcuts import render
from django.conf import settings
from utils import ift
import json
from .models import CtaCert, CtaIdPw
from django.db import IntegrityError
from django.contrib import messages  # 경고창 https://hoy.kr/kxuTa
# model object to dict  https://brownbears.tistory.com/276
from django.forms.models import model_to_dict
from django.views.generic import CreateView  # askdjango 이진석 폼사용
from .forms import CtaIdPwForm               # askdjango 이진석 폼사용

# Create your views here.
# askdjango 이진석 폼사용
ctaidpw_new = CreateView.as_view(model=CtaIdPw, form_class=CtaIdPwForm)

def cert_info(request):
    ctacert_from_db = CtaCert.objects.all()
    context_dict = {'ctacert_from_db': ctacert_from_db}
    # print(context_dict.ctacert_from_db.cert_nm)
    return render(request, 'cert_info.html', context_dict)

def output(request):
    dic_sum = dict()
    dic_1st = dict()
    dic_2nd = dict()
    obj_ctacert = CtaCert.objects.all()   # QuerySet []
    if obj_ctacert:
        lst_dic_ctacert = [model_to_dict(obj) for obj in obj_ctacert[:]]
        lst_cert_nm = [dic_ctacert['cert_nm'] for dic_ctacert in lst_dic_ctacert]
        dic_1st['lst_cert_nm'] = lst_cert_nm
        dic_sum['dic_1st'] = dic_1st
        print(dic_sum)
    else:
        dic_1st['lst_cert_nm'] = ""
        dic_sum['dic_1st'] = dic_1st

    str_cert_info = ift.cert_info()
    dic_cert_info = json.loads(str_cert_info)
    if dic_cert_info['cert_nm'] == "":
        msg = "공인인증서 선택 및 비밀번호 입력후 확인버튼을 누르세요!!!"
        messages.add_message(request, messages.INFO, msg)
        dic_2nd['dic_cert_info'] = dic_cert_info
        dic_sum['dic_2nd'] = dic_2nd
        print(dic_sum)
        return render(request, 'cert_info.html', {'dic_sum': dic_sum})
    try:
        ctacert = CtaCert(**dic_cert_info)  # 인스턴스
        ctacert.save()
        msg = f"인증서 [{dic_cert_info['cert_nm']}] 등록 성공!!!"
        messages.add_message(request, messages.INFO, msg)
        obj_ctacert = CtaCert.objects.all()   # 다시 불러옴
        lst_dic_ctacert = [model_to_dict(obj) for obj in obj_ctacert[:]]
        lst_cert_nm = [dic_ctacert['cert_nm'] for dic_ctacert in lst_dic_ctacert]
        dic_1st['lst_cert_nm'] = lst_cert_nm
        dic_sum['dic_1st'] = dic_1st
        dic_2nd['dic_cert_info'] = dic_cert_info
        dic_sum['dic_2nd'] = dic_2nd

    except IntegrityError as e:
        msg = "이미 저장된 공인인증서 입니다!!!"
        messages.add_message(request, messages.INFO, msg)
        obj_ctacert = CtaCert.objects.all()
        lst_dic_ctacert = [model_to_dict(obj) for obj in obj_ctacert[:]]
        dic_2nd['dic_cert_info'] = dic_cert_info
        dic_sum['dic_2nd'] = dic_2nd
        print(dic_sum)
        return render(request, 'cert_info.html', {'dic_sum': dic_sum})
    print(dic_sum)
    return render(request, 'cert_info.html', {'dic_sum': dic_sum})

"""
def output(request):
    dic_sum = dict()
    dic_1st = dict()
    dic_2nd = dict()
    obj_ctacert = CtaCert.objects.all()   # QuerySet []
    if obj_ctacert:
        lst_dic_ctacert = [model_to_dict(obj) for obj in obj_ctacert[:]]
        lst_cert_nm = [dic_ctacert['cert_nm']
                       for dic_ctacert in lst_dic_ctacert]
        dic_1st['lst_cert_nm'] = lst_cert_nm
        dic_sum['dic_1st'] = dic_1st
        print(dic_sum)
    else:
        dic_1st['lst_cert_nm'] = ""
        dic_sum['dic_1st'] = dic_1st

    str_cert_info = ift.cert_info()
    dic_cert_info = json.loads(str_cert_info)
    if dic_cert_info['cert_nm'] == "":
        msg = "공인인증서 선택 및 비밀번호 입력후 확인버튼을 누르세요!!!"
        messages.add_message(request, messages.INFO, msg)
        dic_2nd['dic_cert_info'] = dic_cert_info
        dic_sum['dic_2nd'] = dic_2nd
        print(dic_sum)
        return render(request, 'cert_info.html', {'dic_sum': dic_sum})
    try:
        ctacert = CtaCert(**dic_cert_info)  # 인스턴스
        ctacert.save()
        msg = f"인증서 [{dic_cert_info['cert_nm']}] 등록 성공!!!"
        messages.add_message(request, messages.INFO, msg)
        obj_ctacert = CtaCert.objects.all()   # 다시 불러옴
        lst_dic_ctacert = [model_to_dict(obj) for obj in obj_ctacert[:]]
        lst_cert_nm = [dic_ctacert['cert_nm']
                       for dic_ctacert in lst_dic_ctacert]
        dic_1st['lst_cert_nm'] = lst_cert_nm
        dic_sum['dic_1st'] = dic_1st
        dic_2nd['dic_cert_info'] = dic_cert_info
        dic_sum['dic_2nd'] = dic_2nd

    except IntegrityError as e:
        msg = "이미 저장된 공인인증서 입니다!!!"
        messages.add_message(request, messages.INFO, msg)
        obj_ctacert = CtaCert.objects.all()
        lst_dic_ctacert = [model_to_dict(obj) for obj in obj_ctacert[:]]
        dic_2nd['dic_cert_info'] = dic_cert_info
        dic_sum['dic_2nd'] = dic_2nd
        print(dic_sum)
        return render(request, 'cert_info.html', {'dic_sum': dic_sum})
    print(dic_sum)
    return render(request, 'cert_info.html', {'dic_sum': dic_sum})
"""
