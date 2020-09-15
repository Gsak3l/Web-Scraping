import multiprocessing
import time

from selenium import webdriver

manager = multiprocessing.Manager()
full_name = manager.list()
email = manager.list()
password = manager.list()
username = manager.list()
bio = manager.list()
verification_code = manager.list()


class Sign_Up_Bot:
    def __init__(self):
        self.bot = webdriver.Firefox()

    def get_mail(self, email_list):  # temporary email address
        bot = self.bot
        bot.get('https://tempail.com/')  # reaching the website
        # getting the value of the input, that contains the email
        local_email = bot.find_element_by_xpath('//*[@id="eposta_adres"]').get_attribute('value')
        email_list.append(local_email)
        print(email_list[len(email_list) - 1])  # printing the email value



    def instagram(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(1)
        bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a/span').click()


if __name__ == '__main__':
    bot1 = Sign_Up_Bot()
    process1 = multiprocessing.Process(target=bot1.get_mail, args=(email,))
    process1.start()
    process1.join()

# Websites used for this autogenerated Instagram bot
# https://tempail.com/ temporary email address
