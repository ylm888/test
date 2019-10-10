from django.core.cache import cache

from common import keys, errors
from lib.http import render_json
from lib.sms import send_sms
from user.models import User


def sendsms(request):
    '''提交手机号，发送验证码'''
    phone = request.GET.get('phone')
    print(phone)
    data = send_sms(phone)
    return render_json(data)
    # return HttpResponse("ok")


def submit_code(request):
    '''提交短信验证码，登录'''
    print("1111111111111111111111")
    phone = request.POST.get('phone')
    vcode = request.POST.get('vcode')


    print(phone,vcode)
    cache_vcode = cache.get(keys.VCODE_KEY % phone)
    # cache_vcode = '2315'
    print(vcode,cache_vcode)
    if vcode == cache_vcode:
        # 执行登录过程
        print("222")
        user,_ = User.objects.get_or_create(phonenum=phone,nickname=phone)

        # 在session中记录登录状态
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    else:
        return render_json("验证码错误",errors.VCODE_ERR)