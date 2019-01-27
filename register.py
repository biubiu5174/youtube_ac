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


class random_account():

    f_fn = open("first_name", "r")
    all_fn = []
    for line in f_fn.readlines():
        if len(line) > 2 and "-" not in line:
            all_fn.append(line.strip())
    f_fn.close()

    f_ln = open("last_name", "r")
    all_ln = []
    for line in f_ln.readlines():
        if len(line) > 2 and "-" not in line:
            all_ln.append(line.strip())
    f_ln.close()


    def first_name(self):
        first_name = random.sample(self.all_fn,1)[0]
        return first_name

    def last_name(self):
        last_name = random.sample(self.all_ln,1)[0]
        return last_name

    def mail_account(self,first_name,last_name):

        mail_name = first_name.lower() + last_name.lower() + ''.join(random.sample(string.digits, 4))
        return mail_name

ra = random_account()


header_dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}




def getRandomString():
    return ''.join(random.sample(string.ascii_letters + string.digits, 8))




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


def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()


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


# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # option.add_argument("--proxy-server=http://103.218.240.182:80")
    driver = webdriver.Chrome(chrome_options=option)
    # 打开chrome浏览器

    # options = webdriver.ChromeOptions()
    #
    # ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A456 MicroMessenger/6.5.7 NetType/WIFI Language/zh_CN'
    #
    # options.add_argument('user-agent=' + ua)
    #
    # driver = webdriver.Chrome(options=options)

    return driver


# 前台开启浏览器模式
def openEdge():
    driver = webdriver.Edge()
    return driver


def register(driver):
    global reginfo, isRelese, isChrome
    headingText = driver.find_element_by_id("headingText")
    if headingText.text == "创建您的 Google 帐号":
        # 找到输入框并输入查询内容
        last_name = driver.find_element_by_id("lastName")
        reginfo['lastName'] = ra.last_name()
        last_name.clear()
        last_name.send_keys(reginfo['lastName'])
        firstName = driver.find_element_by_id("firstName")
        reginfo['firstName'] = ra.first_name()
        firstName.clear()
        firstName.send_keys(reginfo['firstName'])
        user_name = driver.find_element_by_id("username")
        reginfo['username'] = ra.mail_account(reginfo['firstName'],reginfo['lastName'])
        reginfo['email'] = reginfo['username'] + '@gmail.com'
        user_name.clear()
        user_name.send_keys(reginfo['username'])
        passwd = driver.find_element_by_name("Passwd")
        reginfo['password'] = getRandomString()
        passwd.clear()
        passwd.send_keys(reginfo['password'])
        confirm_passwd = driver.find_element_by_name("ConfirmPasswd")
        confirm_passwd.clear()
        confirm_passwd.send_keys(reginfo['password'])
        accountDetailsNext = driver.find_element_by_id("accountDetailsNext")
        # 提交表单
        accountDetailsNext.click()
    elif headingText.text == "验证您的手机号码":
        try:
            code = driver.find_element_by_id("code")
        except NoSuchElementException as e:
            phoneNumberId = driver.find_element_by_id("phoneNumberId")
            if not isRelese:
                ret = releaseNumber()
                if ret:
                    isRelese = True
                    # driver.quit()
                    # openbrowser()
                    # return
                start_timer(driver)
                return
            ret = getPhNumber()
            if not ret:
                start_timer(driver)
                return
            phoneNumberId.clear()
            reginfo['phoneNumber'] = phoneNumber
            phoneNumberId.send_keys('+86 ' + phoneNumber)
            gradsIdvPhoneNext = driver.find_element_by_id("gradsIdvPhoneNext")
            gradsIdvPhoneNext.click()
        else:
            ret = getMsg()
            if not ret:
                start_timer(driver)
                return
            code.send_keys(smsCode)
            reginfo['smsCode'] = smsCode
            gradsIdvVerifyNext = driver.find_element_by_id(
                "gradsIdvVerifyNext")
            gradsIdvVerifyNext.click()
    elif headingText.text == "欢迎使用 Google":
        year = driver.find_element_by_id('year')
        year.send_keys('1988')
        month = driver.find_element_by_id('month')
        month.send_keys('1')
        day = driver.find_element_by_id('day')
        day.send_keys('1')
        gender = driver.find_element_by_id('gender')
        gender.send_keys('不愿透露')
        personalDetailsNext = driver.find_element_by_id('personalDetailsNext')
        personalDetailsNext.click()
    elif headingText.text == "充分利用您的电话号码":
        array = driver.find_elements_by_class_name('uBOgn')
        for i in range(0, len(array)):
            if array[i].text == '跳过':
                array[i].click()
    elif headingText.text == "隐私权及条款":
        # 同意隐私条款后，记录账号信息，重新开启注册页面
        try:
            termsofserviceNext = driver.find_element_by_id(
                'termsofserviceNext')
        except ElementNotVisibleException as e:
            driver.find_element_by_class_name('erm3Qe').click()
            start_timer()
            return
        else:
            while 0 == termsofserviceNext.size['height']:
                try:
                    driver.find_element_by_class_name('erm3Qe').click()
                except Exception as e:
                    break
            file_name = '.\\data\\' + datetime.datetime.now().strftime('%Y%m%d') + '.txt'
            f = open(file_name, 'a', encoding='utf-8')  # 文件路径、操作模式、编码  # r''
            f.write(json.dumps(reginfo) + '\n')
            f.close()
            termsofserviceNext.click()
            reginfo = {}
            operationReg(driver)
            return

    start_timer(driver)

# 注册操作


def operationReg(driver):
    url = "https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com.hk%2Fwebhp%3Fpli%3D1&hl=zh-CN&flowName=GlifWebSignIn&flowEntry=SignUp"
    driver.delete_all_cookies()
    driver.get(url)
    # driver.find_element_by_xpath('//*[@id="1"]/h3/a/em[3]').click()
    # time.sleep(5)
    # driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/content/span').click()
    time.sleep(2)
    start_timer(driver)


def start_timer(driver, time=10):
    print(reginfo)

    f_log = open("gmail_list","a+")

    f_read = open("gmail_list","r")
    all_info = []
    for line in f_read.readlines():
        all_info.append(line.strip())
    f_read.close()
    if "smsCode" in str(reginfo) and str(reginfo) not in all_info:
        f_log.write(str(reginfo)+"\n")
    f_log.close()


    timer = threading.Timer(time, register, (driver,))
    timer.start()


def openbrowser():
    global isChrome
    driver = {}
    if isChrome:
        driver = openChrome()
        isChrome = False
    else:
        driver = openEdge()
        isChrome = True

    operationReg(driver)


# 方法主入口
if __name__ == '__main__':
    ret = smsLogin()
    if ret:
        # 加启动配置
        openbrowser()
