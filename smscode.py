# encoding=utf8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
import time
import threading
import random
import string
from urllib import parse, request
import re
import json
import datetime

reginfo = {
}

token = ""
phoneNumber = ""
smsCode = ""
ITEMID = '147'  # 项目编号
isRelese = True
isChrome = True


header_dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}


def smsLogin():
    global token

    # 登陆/获取TOKEN
    username = 'qiao5174'  # 账号
    password = 'nhZEpdZT9eiQGuU'  # 密码
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=login&username=' + \
        username+'&password='+password
    TOKEN1 = request.urlopen(request.Request(
        url=url, headers=header_dict)).read().decode(encoding='utf-8')
    if TOKEN1.split('|')[0] == 'success':
        TOKEN = TOKEN1.split('|')[1]
        print('TOKEN是'+TOKEN)
        token = TOKEN
        return True
    else:
        print('获取TOKEN错误,错误代码'+TOEKN1+'。代码释义：1001:参数token不能为空;1002:参数action不能为空;1003:参数action错误;1004:token失效;1005:用户名或密码错误;1006:用户名不能为空;1007:密码不能为空;1008:账户余额不足;1009:账户被禁用;1010:参数错误;1011:账户待审核;1012:登录数达到上限')
        return False


def getPhNumber():
    if token.strip():
        global phoneNumber, isRelese
        EXCLUDENO = ''  # 排除号段170_171
        url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token=' + \
            token+'&itemid='+ITEMID+'&excludeno='+EXCLUDENO
        MOBILE1 = request.urlopen(request.Request(
            url=url, headers=header_dict)).read().decode(encoding='utf-8')
        if MOBILE1.split('|')[0] == 'success':
            MOBILE = MOBILE1.split('|')[1]
            print('获取号码是:\n'+MOBILE)
            phoneNumber = MOBILE
            isRelese = False
            return True
        else:
            print('获取TOKEN错误,错误代码'+MOBILE1)
            return False
    else:
        print('获取手机号码失败，token为空重新获取')
        smsLogin()
        return False


def getMsg():
    if token.strip():
        global smsCode
        global isRelese
        TOKEN = token  # TOKEN
        MOBILE = phoneNumber  # 手机号码
        WAIT = 100  # 接受短信时长60s
        url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=' + \
            TOKEN+'&itemid='+ITEMID+'&mobile='+MOBILE+'&release=1'
        text1 = request.urlopen(request.Request(
            url=url, headers=header_dict)).read().decode(encoding='utf-8')
        TIME1 = time.time()
        TIME2 = time.time()
        ROUND = 1
        while (TIME2-TIME1) < WAIT and not text1.split('|')[0] == "success":
            time.sleep(5)
            text1 = request.urlopen(request.Request(
                url=url, headers=header_dict)).read().decode(encoding='utf-8')
            TIME2 = time.time()
            ROUND = ROUND+1

        ROUND = str(ROUND)
        if text1.split('|')[0] == "success":
            text = text1.split('|')[1]
            TIME = str(round(TIME2-TIME1, 1))
            print('短信内容是'+text+'\n耗费时长'+TIME+'s,循环数是'+ROUND)
            start = text.find('G-')
            smsCode = text[(start+2):(start+8)]
            isRelese = True
            return True
        else:
            print('获取短信超时，错误代码是'+text1+',循环数是'+ROUND)
            return False
    else:
        print('获取手机消息失败，token为空重新获取')
        smsLogin()
        return False


def releaseNumber():
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=release&token=' + \
        token+'&itemid='+ITEMID+'&mobile='+phoneNumber

    RELEASE = request.urlopen(request.Request(
        url=url, headers=header_dict)).read().decode(encoding='utf-8')
    if RELEASE == 'success':
        print('号码成功释放:' + phoneNumber)
        return True
    print('号码释放失败：'+RELEASE)
    return False


if __name__ == '__main__':

    smsLogin()
    getPhNumber()
    time.sleep(40)
    getMsg()
    releaseNumber()



