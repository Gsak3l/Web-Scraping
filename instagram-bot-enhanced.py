import multiprocessing
import time
import random

from random import randint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

manager = multiprocessing.Manager()
full_name = manager.list()
email = manager.list()
password = manager.list()
username = manager.list()
bio = manager.list()
verification_code = manager.list()


# noinspection PyBroadException
class Sign_Up_Bot:
    def __init__(self):
        self.bot = webdriver.Firefox()

    def get_mail(self, email_list):  # temporary email address
        bot = self.bot
        bot.get('https://tempail.com/')  # reaching the website
        # getting the value of the input, that contains the email and storing it to our global list
        email_list.append(bot.find_element_by_xpath('//*[@id="eposta_adres"]').get_attribute('value'))
        print(email_list[len(email_list) - 1])  # printing the email value

    def get_full_name(self, full_name_list):  # random generated name
        bot = self.bot
        bot.get('https://www.name-generator.org.uk/quick/')  # reaching the website
        # getting a random name from a random generated name table
        full_name_list.append(bot.find_elements_by_class_name('name_heading')[randint(0, 9)].text)
        print(full_name_list[len(full_name_list) - 1])  # printing the email value
        bot.close()

    def get_full_greek_name(self, full_name_list):  # random generated name
        bot = self.bot
        bot.get('https://www.fantasynamegenerators.com/greek_names.php')  # reaching the website
        # deciding between male and female names
        flag = True
        # keep trying while it clicks one of the two buttons, either for a male or a female name
        while flag:
            try:
                # trying to click the button
                bot.find_element_by_xpath(
                    '/html/body/div[2]/div[2]/div/div[4]/div[1]/input[' + str(randint(1, 2)) + ']').click()
                # taking all the names, and giving them to the names variable
                names = bot.find_element_by_id('result').text
                # storing one random name to our global name list
                full_name_list.append(names.split('\n')[randint(0, 9)])
                flag = False
            except:
                pass
        # printing the name stored
        print(full_name_list[len(full_name_list) - 1])
        bot.close()

    def get_username(self, username_list):  # generating a username with the given full name
        bot = self.bot
        bot.get('https://www.name-generator.org.uk/username/')  # reaching the website
        # waiting to get the full name first
        flag = True
        while flag:
            if len(full_name) > 0:
                print(full_name[0].split(' ')[0])
                print(full_name[0].split(' ')[1])
                try:
                    # clicking the cookie thing
                    bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/button[2]').click()
                except:
                    pass
                try:
                    # closing an advertisement
                    bot.find_element_by_class_name('dmCatClose').click()
                except:
                    pass
                    flag = False
        # getting all the buttons with the class button
        buttons = bot.find_elements_by_class_name('button')
        for button in buttons:
            # clicking only the buttons with the text Suggest
            if button.get_attribute('value') == 'Suggest':
                button.click()
                bot.execute_script('window.scrollBy(0, 30);')
        # from all the suggestions, blanking the first, last name, and middle name
        bot.find_elements_by_class_name('sizeMedium')[0].clear()
        bot.find_elements_by_class_name('sizeMedium')[1].clear()
        bot.find_elements_by_class_name('sizeMedium')[2].clear()
        # adding the name from the full_name list
        bot.find_elements_by_class_name('sizeMedium')[0].send_keys(full_name[0].split(' ')[0])
        bot.find_elements_by_class_name('sizeMedium')[2].send_keys(full_name[0].split(' ')[1])
        # clicking the create submit form button
        bot.find_element_by_class_name('create_form_submit').click()
        # storing one random username to our global username list
        username_list.append(bot.find_elements_by_class_name('username_item')[randint(0, 5)].text)
        # printing the stored username
        print(username_list[len(username_list) - 1])
        bot.close()

    def get_password(self, password_list):  # generating a random password
        bot = self.bot
        bot.get('https://www.avast.com/random-password-generator')  # reaching the website
        bot.find_elements_by_class_name('checkmark')[3].click()  # clicking the symbols
        for i in range(randint(0, 5)):
            if bool(random.getrandbits(1)):  # random true false generator
                # increasing the password length when it's true
                bot.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/section[1]/div/div[2]/div[2]/div[1]/div[1]').click()
            else:
                # decreasing the password length when it's false
                bot.find_element_by_xpath(
                    '/html/body/div[3]/div[2]/div/section[1]/div/div[2]/div[2]/div[1]/div[2]').click()
        # storing one random password to our global password list
        password_list.append(bot.find_elements_by_class_name('password')[0].text)
        # printing the stored password
        print(password_list[len(password_list) - 1])
        bot.close()

    def instagram(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/emailsignup/')  # reaching instagram
        flag = True
        while flag:  # moving forward only when we have pwd, name, username, and email saved on the globals
            if len(full_name) > 0 and len(email) > 0 and len(username) > 0 and len(password) > 0:
                flag = False
        flag = True
        while flag:
            try:
                bot.find_element_by_name('emailOrPhone').send_keys(email[len(email) - 1])  # input email
                bot.find_element_by_name('fullName').send_keys(full_name[len(full_name) - 1])  # input name
                bot.find_element_by_name('username').send_keys(username[len(username) - 1])  # input username
                bot.find_element_by_name('password').send_keys(password[len(password) - 1])  # input password
                flag = False
            except:
                pass
        # clicking the next button on the credential form
        buttons = bot.find_elements_by_tag_name('button')
        for button in buttons:
            if button.text == 'Sign up' or button.text == 'Next':
                button.click()
        time.sleep(1)
        # checking if we get an error for the username of the account
        try:
            # checking if this paragraph exists anywhere, if it does, the name should be changed
            print(bot.find_element_by_xpath('//*[@id="ssfErrorAlert"]').text)
            spans = bot.find_elements_by_tag_name('span')
            for span in spans:
                if span.text == 'Refresh suggestion':  # using instagram username generator if username exists
                    span.click()
            for button in buttons:  # clicking the next button once again
                if button.text == 'Sign up' or button.text == 'Next':
                    button.click()
        except:
            pass
        time.sleep(1)
        # selecting random age
        # selecting a year between 1975 and 2001 (18+ years old)
        year = Select(bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select'))
        year.select_by_value(str(randint(1975, 2001)))
        # selecting a random month between january and december
        month = Select(bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select'))
        month.select_by_value(str(randint(1, 12)))
        # month, but i have to consider what month has 28 or 30 days and what month has 31 days
        flag = True
        day = Select(bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select'))
        while flag:
            try:
                day.select_by_value(str(randint(1, 31)))
                flag = False
            except:
                pass
        # please work please work please work


if __name__ == '__main__':
    bot1 = Sign_Up_Bot()
    bot2 = Sign_Up_Bot()
    bot3 = Sign_Up_Bot()
    bot4 = Sign_Up_Bot()
    bot5 = Sign_Up_Bot()
    process1 = multiprocessing.Process(target=bot1.get_mail, args=(email,))
    process2 = multiprocessing.Process(target=bot2.get_full_name, args=(full_name,))
    process3 = multiprocessing.Process(target=bot3.get_username, args=(username,))
    process4 = multiprocessing.Process(target=bot4.get_password, args=(password,))
    process5 = multiprocessing.Process(target=bot5.instagram, )
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()

# Websites used for this autogenerated Instagram bot
# https://tempail.com/ temporary email address
# https://www.fantasynamegenerators.com/greek_names.php greek name generator
# https://www.name-generator.org.uk/quick/ world wide name generator
# https://www.name-generator.org.uk/username/ username generator
# ---------------------------------------------------------------
