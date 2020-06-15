from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import multiprocessing

manager = multiprocessing.Manager()
shared_stuff = manager.list()


class Sign_Up_Bot:
    def __init__(self):  # constructor
        self.bot = webdriver.Firefox()  # opens firefox in this case

    def get_email(self, list):
        bot = self.bot
        bot.get("https://tempail.com/en/")
        time.sleep(3)  # waiting 3 seconds to connect to the site
        email = bot.find_element_by_xpath('//*[@id="eposta_adres"]').get_attribute(
            "value")  # getting the temp mail for the sign-up
        list.append(email)
        flag = True
        while flag:
            try:
                # trying to get the email code that tweeter will send us
                verification_code = bot.find_element_by_xpath(
                    '/html/body/section[2]/div/div/div/ul/li[2]/a/div[3]').text
                verification_code = int(verification_code.split()[0])  # splitting just the numbers
                flag = False
            except:
                pass
        # bot.close()

    def get_full_name(self, list):
        bot = self.bot
        bot.get("https://www.behindthename.com/random/")
        time.sleep(3)
        bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/center/form/div/input').click()  # clicking generate name button
        full_name = bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/center/div[1]/span/a[1]').text + " " + bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/center/div[1]/span/a[2]').text  # getting the full name from the proper website
        list.append(full_name)

    def get_password(self, list):
        bot = self.bot
        bot.get("https://nordpass.com/password-generator/")
        time.sleep(3)
        # getting the random generated password
        password = bot.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/main/div/div[5]/section/div/div/div/div[1]/div/div[1]/div[1]').text
        list.append(password)

    def createTwitterAccount(self, list):
        bot = self.bot
        bot.get("https://twitter.com/explore")
        time.sleep(3)
        # clicking the sign up button
        bot.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[2]/header/div[2]/div[1]/div/div[2]/div[1]/div[2]/a').click()
        time.sleep(0.5)  # waiting fot the form to appear
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/'
                                  'div[2]/div/div/div[4]/span').click()  # clicking the email option instead of phone
        # giving to the username input, the right value
        bot.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]'
            '/label/div/div[2]/div/input').send_keys(full_name)
        time.sleep(0.5)
        # giving to the email input the right value
        bot.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/'
            'div/div/div[3]/label/div/div[2]/div/input').send_keys(email)
        time.sleep(1)
        # clicking the next button at the top right corner to get to the next page
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]'
                                  '/div[1]/div/div/div/div[3]/div').click()
        time.sleep(0.5)
        # clicking personalized ads, twitter connections, and receiving twitter notifications on email
        # this way the account has a smaller chance of getting banned
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/'
                                  'div[2]/div/div/label[1]/div[2]/input').click()
        time.sleep(0.2)
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/'
                                  'div[2]/div/div/label[2]/div[2]/input').click()
        time.sleep(0.2)
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/'
                                  'div[2]/div/div/label[3]/div[2]/input').click()
        time.sleep(0.2)
        # clicking the next button at the top right corner to get to the next page
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/'
                                  'div[1]/div/div/div/div[3]/div').click()
        time.sleep(0.5)
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/'
                                  'div[2]/div/div/div/div[4]/div').click()


if __name__ == '__main__':
    bot1 = Sign_Up_Bot()
    bot2 = Sign_Up_Bot()
    bot3 = Sign_Up_Bot()
    process1 = multiprocessing.Process(target=bot1.get_full_name, args=(shared_stuff,))
    process2 = multiprocessing.Process(target=bot2.get_email, args=(shared_stuff,))
    process3 = multiprocessing.Process(target=bot3.get_password, args=(shared_stuff,))
    process1.start()
    process2.start()
    process3.start()
    process1.join()
    process2.join()
    process3.join()
    # print("Full Name: " + full_name + " Email Address: " + email + " Password: " + password)
    print(shared_stuff)

# websites used for this autogenerated-twitter like bot
# https://tempail.com/en/ temporary email address
# https://www.behindthename.com/random/ random name
# https://nordpass.com/password-generator/ random password
# https://twitter.com/explore twitter
