from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import multiprocessing
from selenium.webdriver.support.ui import Select
from random import randint

manager = multiprocessing.Manager()
full_name = manager.list()
email = manager.list()
password = manager.list()
verification_code = manager.list()
bio = manager.list()


class Sign_Up_Bot:
    def __init__(self):  # constructor
        self.bot = webdriver.Firefox()  # opens firefox in this case

    def get_email(self, email_list):
        bot = self.bot
        bot.get("https://tempail.com/en/")
        time.sleep(3)  # waiting 3 seconds to connect to the site
        local_email = bot.find_element_by_xpath('//*[@id="eposta_adres"]').get_attribute(
            "value")  # getting the temp mail for the sign-up
        email_list.append(local_email)
        local_verification_code = ""
        flag = True
        while flag:
            try:
                # trying to get the email code that tweeter will send us
                local_verification_code = bot.find_element_by_xpath(
                    '/html/body/section[2]/div/div/div/ul/li[2]/a/div[3]').text
                local_verification_code = int(local_verification_code.split()[0])  # splitting just the numbers
                flag = False
            except:
                pass
        verification_code.append(local_verification_code)
        bot.close()

    def get_full_name(self, full_name_list):
        bot = self.bot
        bot.get("https://www.behindthename.com/random/")
        time.sleep(3)
        bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/center/form/div/input').click()  # clicking generate name button
        local_full_name = bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/center/div[1]/span/a[1]').text + " " + bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/center/div[1]/span/a[2]').text  # getting the full name from the proper website
        full_name_list.append(local_full_name)
        bot.close()

    def get_password(self, password_list):
        bot = self.bot
        bot.get("https://nordpass.com/password-generator/")
        time.sleep(3)
        # getting the random generated password
        local_password = bot.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div/div[1]/main/div/div[4]/section/div/div/div/div[1]/div/div[1]/div[1]').text
        password_list.append(local_password)
        bot.close()

    def get_bio(self, bio_list):
        bot = self.bot
        bot.get('https://sassycaptions.com/bio-generator/')
        time.sleep(1)
        # cookie stuff
        bot.find_element_by_xpath('//*[@id="onesignal-popover-cancel-button"]').click()
        time.sleep(0.5)
        # generating a bio
        bot.find_element_by_xpath('//*[@id="gen"]').click()
        # taking the bio
        bio_list.append(bot.find_element_by_xpath('//*[@id="quote"]').text)

    def twitter_bot(self):
        bot = self.bot
        bot.get("https://twitter.com/explore")
        time.sleep(3)
        flag = True
        while flag:
            if len(full_name) > 0 and len(email) > 0 and len(password) > 0:
                # clicking the sign up button
                bot.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[2]/header/div[2]/div[1]/div/div[2]/div[1]/div[2]/a').click()
                time.sleep(0.5)  # waiting for the form to appear
                bot.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/'
                    'div[2]/div/div/div[4]/span').click()  # clicking the email option instead of phone
                # giving to the username input, the right value
                bot.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/'
                    'div/div[2]/label/div/div[2]/div/input').send_keys(full_name[0])
                time.sleep(0.5)
                # giving to the email input the right value
                bot.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/'
                    'div/div/div[3]/label/div/div[2]/div/input').send_keys(email[0])
                time.sleep(1)
                # adding the age on the fields
                # month
                select = Select(bot.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                    '2]/div/div/div[5]/div[3]/div/div[1]/div[2]/select'))
                select.select_by_value(str(randint(1, 12)))
                time.sleep(0.2)
                # day
                select = Select(bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div['
                                                          '2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div['
                                                          '3]/div/div[2]/div[2]/select'))
                select.select_by_value(str(randint(1, 30)))
                time.sleep(0.2)
                # year
                select = Select(bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div['
                                                          '2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div['
                                                          '3]/div/div[3]/div[2]/select'))
                select.select_by_value(str(randint(1960, 2001)))
                time.sleep(0.5)
                # clicking the next button at the top right corner to get to the next page
                bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div['
                                          '2]/div/div/div[2] '
                                          '/div[1]/div/div/div/div[3]/div').click()
                time.sleep(0.5)
                # accepting some options like personalized ads etc
                for i in range(1, 4):
                    bot.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/'
                        'div/div/label[' + str(i) + ']/div[2]/input').click()
                    time.sleep(1)
                # clicking the next button at the top right corner to get to the next page
                bot.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/'
                    'div[1]/div/div/div/div[3]/div').click()
                time.sleep(0.5)
                bot.find_element_by_xpath(  # clicking the final sign-up button
                    '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                    '2]/div/div/div/div[5]/div').click()
                flag2 = True
                while flag2:
                    if len(verification_code) > 0:
                        time.sleep(0.5)
                        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div['
                                                  '2]/div/div/div[2]/div[2]/div/div/div/div[2]/label/div'
                                                  '/div[2]/div/input').send_keys(verification_code[0])
                        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/'
                                                  'div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
                        time.sleep(0.5)
                        flag2 = False
                time.sleep(0.5)
                # typing the password
                bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/'
                                          'div[2]/div[2]/div/div/div[3]/div/label/div/div[2]/div/'
                                          'input').send_keys(password[0])
                time.sleep(2)
                # clicking the next button at the top right corner to get to the next page
                bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div['
                                          '2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
                time.sleep(2)
                # skipping the add profile picture option
                bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div['
                                          '2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/span/span').click()
                time.sleep(2)
                # skipping the bio option
                bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div['
                                          '2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/span/span').click()
                time.sleep(2)
                # skipping the interests
                bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div['
                                          '2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div').click()
                time.sleep(2)
                # following some accounts
                for i in range(3, 13):
                    bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div/'
                                              'div[2]/div[2]/div/div/div[3]/section/div/div/div/div[' + str(i) +
                                              ']/div/div/div/div[2]/div[1]/div[2]/div').click()
                time.sleep(2)
                # clicking the final follow button
                bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div['
                                          '2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
                time.sleep(2)
                # clicking the skip for now button for the notifications
                bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div['
                                          '2]/div/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div').click()
                time.sleep(2)
                flag = False
                # and the account has been created
                f = open("accounts.txt", "a+")
                f.write("Full Name: " + full_name[0] + " || Email: " + email[0] + " || Password: " + password[0] + "\n")
                f.close()
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]').click()
        time.sleep(2)
        flag = True
        counter = 1
        tries = []
        while flag:
            try:
                tries.append(counter)
                if tries.count(counter) == 5:
                    counter += 1
                    bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                    time.sleep(2)
                else:
                    bot.find_element_by_xpath(
                        '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div['
                        '4]/div/div/section/div/div/div/div[ '
                        + str(counter) + ']/div/div/div/div/article/div/div[2]/div[2]/div[2]/div[3]/div[3]'
                                         '/div/div/div[1]').click()
                    counter += 1
                    time.sleep(1)
            except:
                pass


if __name__ == '__main__':
    # creating 4 different bots, who have 4 different processes
    bot1 = Sign_Up_Bot()
    bot2 = Sign_Up_Bot()
    bot3 = Sign_Up_Bot()
    bot4 = Sign_Up_Bot()
    bot5 = Sign_Up_Bot()
    process1 = multiprocessing.Process(target=bot1.get_full_name, args=(full_name,))
    process2 = multiprocessing.Process(target=bot2.get_email, args=(email,))
    process3 = multiprocessing.Process(target=bot3.get_password, args=(password,))
    process4 = multiprocessing.Process(target=bot4.get_bio, args=(bio,))
    process5 = multiprocessing.Process(target=bot5.twitter_bot, )
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    print(bio[0])
    # input_1 = raw_input("1. Like All the Posts from the Home Page\n"
    #                     "2. Retweet All the Posts from the Home Page\n"
    #                     "3. Like All the Posts from a specific Hashtag #\n"
    #                     "4. Like a Specific Post\n"
    #                     "Please Type your Answer Here: ")

# this bot creates accounts only in Europe. US has an age restriction, and I didn't scrape that part
# websites used for this autogenerated-twitter like bot
# https://tempail.com/en/ temporary email address
# https://www.behindthename.com/random/ random name
# https://nordpass.com/password-generator/ random password
# https://sassycaptions.com/bio-generator/ generating bio
# https://twitter.com/explore twitter
# please note, that twitter might ask some of these accounts to fill a phone number
