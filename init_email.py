from selenium import webdriver
from selenium.webdriver.support.select import Select
import os
import re
import time
import hashlib
import traceback
# f_path = r'c:\a.txt'
# f = open (f_path, "r+")
# open('c:\\a1.txt', 'w').write(re.sub(r'hello world', 'Love python', f.read()))


class InitEmail():

    driver = webdriver.Chrome()
    def change_password(self,email,password):
        """
        # change password
        # delete phone
        # open youtube channel
        # name and head picture
        #
        :return: 
        """
        # 读入文件
        f = open("temp","r")

        # for line in f.readlines():
        #     email = eval(line)["email"]
        #     password = eval(line)["password"]
        print(email, password)
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.get("https://accounts.google.com/")

        email_input = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_input.send_keys(email)

        next_step = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
        next_step.click()

        time.sleep(2)

        password_input = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password_input.send_keys(password)

        try:
            page_title = self.driver.find_element_by_tag_name('h1').text
            if page_title == '请验证您的身份':
                time.sleep(100)

        except:

            print("vertify not found")


        next_step = self.driver.find_element_by_class_name('CwaK9')
        next_step.click()

        time.sleep(15)

        # person center
        # click the tag

        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/c-wiz/c-wiz/div/div[3]/c-wiz/div/a[2]/div[2]').click()
        self.driver.implicitly_wait(30)
        # change password #######################################
        self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/c-wiz/c-wiz/div/div[4]/div/div/c-wiz/section/article[1]/div/div/div[6]/div[2]/a/div/div[1]/div/div[2]/div[1]/div').click()

        password_input = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password_input.send_keys(password)

        next_step = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
        next_step.click()
        self.driver.implicitly_wait(30)

        new_password = hashlib.md5(email.strip().encode('utf-8')).hexdigest()[0:13]
        print(new_password)

        new_password_input = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/c-wiz/div/div[3]/div[1]/c-wiz/form/div[1]/div/div[1]/div/div[1]/input')
        new_password_input.send_keys(new_password)

        confirm_password = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/c-wiz/div/div[3]/div[1]/c-wiz/form/div[3]/div/div[1]/div/div[1]/input')
        confirm_password.send_keys(new_password)

        change_button = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/c-wiz/div/div[3]/div[2]/div/content/span')
        change_button.click()
        self.driver.implicitly_wait(30)

        time.sleep(10)
        # change the password record
        # open('temp', 'w').write(re.sub(password, new_password, f.read()))
        self.driver.quit()


    def login(self,email,password):
        self.driver.delete_all_cookies()
        self.driver.get("https://accounts.google.com/")

        email_input = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_input.send_keys(email)

        next_step = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
        next_step.click()

        time.sleep(2)

        password_input = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password_input.send_keys(password)

        next_step = self.driver.find_element_by_class_name('CwaK9')
        next_step.click()

        time.sleep(2)
        # self.driver.find_element_by_xpath("//*[contains(text(), '个人信息')]").click()
        self.driver.find_element_by_xpath(
            '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/c-wiz/c-wiz/div/div[3]/c-wiz/div/a[2]/div[2]').click()
        time.sleep(2)





    def dele_phone(self,email,password):

        # self.login(email,password)

        try:
            self.driver.find_element_by_xpath(
                '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/c-wiz/c-wiz/div/div[3]/c-wiz/div/a[2]/div[2]').click()
            self.driver.implicitly_wait(30)
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)

            contact_info = self.driver.find_elements_by_class_name('GIxHAe')[1]

            self.driver.find_element_by_xpath("//*[contains(text(), '电话')]").click()
            time.sleep(2)

            self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/c-wiz/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/content/span/span').click()

            try:
                password_input = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
                password_input.send_keys(password)

                next_step = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
                next_step.click()

            except:
                print("haha")

            dele_step = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/c-wiz/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/content/span/span')
            dele_step.click()

            dele_confirm = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[11]/div/div[2]/div[3]/div[2]/content/span')
            dele_confirm.click()

            # go back

            self.driver.find_element_by_xpath('//*[@id="sdgBod"]/span[1]').click()


        except Exception as e:
            print('fuck')
            traceback.print_exc()


    def dele_email(self,email,password):

        # self.login(email, password)

        try:
            time.sleep(10)
            self.driver.implicitly_wait(30)
            # self.driver.find_element_by_xpath("//*[contains(text(), '个人信息')]").click()

            self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/c-wiz/c-wiz/div/div[3]/c-wiz/div/a[2]/div[2]').click()

            self.driver.find_element_by_xpath("//*[contains(text(), '电子邮件')]").click()

            self.driver.find_element_by_xpath("//*[contains(text(), '辅助邮箱')]").click()

            # enter the password

            password_input = self.driver.find_element_by_class_name("Xb9hP").find_element_by_tag_name('input')
            password_input.send_keys(password)

            next_step = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
            next_step.click()


            # click to edit
            edit_icon  = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/c-wiz/div/div[3]/div[1]/div/div[2]/content/span/span')
            edit_icon.click()

            edit_email = self.driver.find_element_by_class_name('Xb9hP').find_element_by_tag_name('input')
            edit_email.clear()


            self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[11]/div/div[2]/div[3]/div[2]/content/span').click()


            # gtcbvuqz
            print("email alredy dele.....")


        except Exception as e:
            traceback.print_exc()




    def google_passport(self):

        # email = "rgtzb7kp@gmail.com"
        # password = 'meituanbaidu2'

        f = open('gmail_list',"r")
        for line in f.readlines():
            email = eval(line)['email']
            password = eval(line)['password']
            print(email,password)

            new_password = hashlib.md5(email.strip().encode('utf-8')).hexdigest()[0:13]

            self.change_password(email,password)
            # self.dele_phone(email,new_password)
            # self.dele_email(email,new_password)

            print(email,"new_password:",new_password)




class youtube_ac_vertify():
    driver = webdriver.Chrome()





if __name__ == '__main__':
    ie = InitEmail()
    # ie.google_passport()


    # ie.dele_phone("rgtzb7kp@gmail.com","0209236cd")

    # ie.dele_email("ssllnl05@gmail.com",'gtcbvuqz')

    ie.google_passport()

    # ie.change_password()
