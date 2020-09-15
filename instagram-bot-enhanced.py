import multiprocessing
import time
from random import randint

from selenium import webdriver

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
        # waiting to get the full name first
        flag = True
        while flag:
            if len(full_name) > 0:
                print(full_name[0].split(' ')[0])
                print(full_name[0].split(' ')[1])
                bot.get('https://www.name-generator.org.uk/username/')  # reaching the website
                try:
                    # clicking the cookie thing
                    bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/button[2]').click()
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

    def get_mail(self, email_list):  # temporary email address
        bot = self.bot
        bot.get('https://tempail.com/')  # reaching the website
        # getting the value of the input, that contains the email and storing it to our global list
        email_list.append(bot.find_element_by_xpath('//*[@id="eposta_adres"]').get_attribute('value'))
        print(email_list[len(email_list) - 1])  # printing the email value

    def instagram(self):
        bot = self.bot
        flag = True
        while flag:
            if len(full_name) > 0 and len(email) > 0 and len(username) > 0 and len(password) > 0:
                bot.get('https://www.instagram.com/')
                time.sleep(1)
                bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a/span').click()
                flag = False


if __name__ == '__main__':
    bot1 = Sign_Up_Bot()
    bot2 = Sign_Up_Bot()
    bot3 = Sign_Up_Bot()
    process1 = multiprocessing.Process(target=bot1.get_mail, args=(email,))
    process2 = multiprocessing.Process(target=bot2.get_full_name, args=(full_name,))
    process3 = multiprocessing.Process(target=bot3.get_username, args=(username,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    process3.start()
    process3.join()

# Websites used for this autogenerated Instagram bot
# https://tempail.com/ temporary email address
# https://www.fantasynamegenerators.com/greek_names.php greek name generator
