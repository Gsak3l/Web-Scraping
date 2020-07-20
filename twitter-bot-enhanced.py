import multiprocessing
import os
import time
import urllib.request
from random import randint
from selenium import webdriver
from selenium.webdriver.support.ui import Select

manager = multiprocessing.Manager()
full_name = manager.list()
email = manager.list()
password = manager.list()
verification_code = manager.list()
bio = manager.list()
errors = manager.list()
log_flag = manager.list()


# noinspection PyBroadException
class Tweet_Bot:
    def __init__(self):  # constructor
        self.bot = webdriver.Firefox()

    def sign_in(self, local_log_flag):
        # this entire def is made because twitter asks for a second verification code when creating a new account
        # and then trying to log in :X
        bot = self.bot
        flag = True
        while flag:
            if len(log_flag) == 1:
                bot.get('https://twitter.com/login')
                time.sleep(1)
                bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div['
                                          '2]/div/input').send_keys(email[0])
                bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div['
                                          '2]/div/input').send_keys(password[0])
                # pressing the log in button
                bot.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()
                log_flag.append(True)
                flag = False
        flag = True
        while flag:
            if len(verification_code) == 2:
                bot.find_element_by_xpath('//*[@id="challenge_response"]').send_keys(verification_code[1])
                bot.find_element_by_xpath('//*[@id="email_challenge_submit"]').click()
                flag = False

    def tweet_inspirational_quote(self):
        bot = self.bot
        bot.get('https://randomwordgenerator.com/motivational-quote.php')  # the website the quote
        time.sleep(1.5)  # waiting for the quote to appear
        quote = bot.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[2]/div/ol/li/div/span').text
        quote += "\n"  # breaking line
        # getting the top hashtags for the day
        bot.get('https://www.tweeplers.com/hashtags/?cc=WORLD')
        hashtag_counter = randint(1, 10)
        for i in range(hashtag_counter):
            num = randint(2, 21)
            if num != 7:
                quote += bot.find_element_by_xpath(
                    '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[' + str(num) + ']/div[2]/a[1]/b').text + "\n"
        # twitter
        bot.get('https://twitter.com/login')
        time.sleep(1)
        # filling username and password
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div['
                                  '2]/div/input').send_keys(email[0])
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div['
                                  '2]/div/input').send_keys(password[0])
        # pressing the log in button
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()
        # cookie thing
        bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div/span/span').click()
        time.sleep(1)
        # pressing the tweet button
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
        time.sleep(0.3)
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div['
                                  '3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/'
                                  'div/div/div[1]/div/div/div/div[2]/div').send_keys(quote)
        # twitting the quote
        bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div['
                                  '3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]').click()

    def like_tweets(self):
        bot = self.bot
        # twitter
        bot.get('https://twitter.com/login')
        time.sleep(1)
        # filling username and password
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div['
                                  '2]/div/input').send_keys(email[0])
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div['
                                  '2]/div/input').send_keys(password[0])
        # pressing the log in button
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()
        time.sleep(1)
        # cookie thing
        bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div/span/span').click()
        # liking random things things
        rng = randint(10, 20)
        for i in range(1, rng):
            try:
                # trying to make random like choices
                bot.find_element_by_xpath(
                    '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[4]/div/div/section/div/div/'
                    'div/div[' + str(randint(1, rng)) + ']/div/div/article/div/div/div/div[2]/div[2]/div[2]/'
                                                        'div[3]/div[3]/div/div/div[1]').click()
                time.sleep(0.5)
            except:
                pass

    def follow_random_users(self):
        bot = self.bot
        # twitter
        bot.get('https://twitter.com/login')
        time.sleep(1)
        # filling username and password
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div['
                                  '2]/div/input').send_keys(email[0])
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div['
                                  '2]/div/input').send_keys(password[0])
        # pressing the log in button
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()
        time.sleep(1)
        # cookie thing
        bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div/span/span').click()
        # scrolling by some pixels
        bot.execute_script('window.scrollTo(0, 50)')
        time.sleep(0.5)
        # clicking the show more on the follow section
        bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div['
                                  '2]/div/div/div/div[4]/aside/a/div/span').click()
        time.sleep(1.5)
        # following random users
        # because you follow part: 1, more
        container = bot.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]')
        elements = container.find_elements_by_xpath('//span[contains(text(), "More")]')
        for i in range(1, len(elements)):
            try:
                elements[i].click()
                time.sleep(2)
                bot.back()
                print(i)
            except:
                pass


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
        while len(errors) == 0 and flag:
            # noinspection PyBroadException
            try:
                # trying to get the email code that tweeter will send us
                local_verification_code = bot.find_element_by_xpath(
                    '/html/body/section[2]/div/div/div/ul/li[2]/a/div[3]').text
                local_verification_code = int(local_verification_code.split()[0])  # splitting just the numbers
                flag = False
            except:
                pass
        verification_code.append(local_verification_code)
        flag = True
        while flag:
            # if we disconnect from twitter and reconnect, twitter asks for a second verification code
            # it is painful, but i think it works
            if len(log_flag) == 2:
                time.sleep(15)
                bot.find_element_by_xpath('/html/body/section[2]/div/div/div/ul/li[2]/a').click()
                time.sleep(3)
                bot.switch_to.frame(bot.find_element_by_xpath('//*[@id="iframe"]'))
                verification_code.append(bot.find_element_by_xpath(
                    '/html/body/table/tbody/tr[2]/td/table[2]/tbody/tr[1]/td[2]/table/tbody/tr[7]/td/strong').text)
                flag = False
        bot.close()

    def get_full_name(self, full_name_list):
        bot = self.bot
        bot.get("https://www.behindthename.com/random/random.php?number=2&sets=1&gender=both&surname=&all=yes")
        local_full_name = bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/center/div[1]/span/a[1]').text + " " + bot.find_element_by_xpath(
            '/html/body/div[2]/div/div/center/div[1]/span/a[2]').text  # getting the full name from the proper website
        full_name_list.append(local_full_name)
        bot.close()

    def get_profile_picture(self):
        bot = self.bot
        bot.get('https://thispersondoesnotexist.com/image')
        bot.save_screenshot('image.png')  # saving a screenshot of an image
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
        bot.close()

    def create_twitter_account(self, error_list, local_log_flag):
        bot = self.bot
        bot.get("https://twitter.com/explore")
        time.sleep(3)
        flag = True
        while flag:
            if len(full_name) > 0 and len(email) > 0 and len(password) > 0:
                try:
                    # clicking the sign up button
                    bot.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[2]/header/div[2]/div[1]/div/div[2]/div[1]/div[2]/a').click()
                    time.sleep(0.5)  # waiting for the form to appear
                    bot.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                        '2]/div[2]/div/div/div[4]/span').click()  # clicking the email option instead of phone
                    # giving to the username input, the right value
                    bot.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                        '2]/div[2]/div/div/div[2]/label/div/div[2]/div/input').send_keys(full_name[0])
                    time.sleep(0.5)
                    # giving to the email input the right value
                    bot.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                        '2]/div[2]/div/div/div[3]/label/div/div[2]/div/input').send_keys(email[0])
                    time.sleep(1)
                    # adding the age on the fields
                    # month
                    select = Select(bot.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                        '2]/div[2]/div/div/div[5]/div[3]/div/div[1]/div[2]/select'))
                    select.select_by_value(str(randint(1, 12)))
                    time.sleep(0.2)
                    # day
                    select = Select(bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div['
                                                              '2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                                              '2]/div[2]/div/div/div[5]/div[3]/div/div[2]/div['
                                                              '2]/select'))
                    select.select_by_value(str(randint(1, 30)))
                    time.sleep(0.2)
                    # year
                    select = Select(bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div['
                                                              '2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                                              '2]/div[2]/div/div/div[5]/div[3]/div/div[3]/div['
                                                              '2]/select'))
                    select.select_by_value(str(randint(1960, 2001)))
                    time.sleep(0.5)
                    # clicking the next button at the top right corner to get to the next page
                    bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div['
                                              '2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
                    time.sleep(0.5)
                    # accepting some options like personalized ads etc
                    try:
                        for i in range(1, 4):
                            bot.find_element_by_xpath(
                                '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                '2]/div/div/div[2]/div[2]/div/div/label[' + str(i) + ']/div[2]/input').click()
                            time.sleep(0.3)
                    except:
                        pass
                    # clicking the next button at the top right corner to get to the next page
                    bot.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                        '2]/div[1]/div/div/div/div[3]/div').click()
                    time.sleep(0.5)
                    bot.find_element_by_xpath(  # clicking the final sign-up button
                        '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                        '2]/div[2]/div/div/div/div[5]/div').click()
                    flag2 = True
                    while flag2:
                        if len(verification_code) > 0:
                            time.sleep(0.5)
                            bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div['
                                                      '2]/div[2]/div/div/div[2]/div[2]/div/div/div/div['
                                                      '2]/label/div/div[2]/div/input').send_keys(verification_code[0])
                            time.sleep(0.5)
                            bot.find_element_by_xpath(
                                '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                '2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
                            flag2 = False
                    time.sleep(0.5)
                    # typing the password
                    bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div['
                                              '2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/label/div/div['
                                              '2]/div/input').send_keys(password[0])
                    time.sleep(2)
                    # clicking the next button at the top right corner to get to the next page
                    bot.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div['
                                              '2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
                    time.sleep(2)
                    # adding picture option with a relative path, the stock path is the project path
                    bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                              '2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/div['
                                              '3]/input').send_keys(os.getcwd() + "/image.png")
                    # to match the path of the image from your computer
                    time.sleep(0.5)
                    bot.find_element_by_xpath(
                        '/html/body/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div/div['
                        '1]/div/div/div/div[3]/div').click()  # pressing apply on the aspect ratio
                    time.sleep(1)
                    # pressing the next button
                    bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                              '2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
                    time.sleep(2)
                    # adding the bio
                    bot.find_element_by_xpath(
                        '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                        '2]/div/div/div[3]/label/div/div[2]/div/textarea').send_keys(bio[0])
                    # pressing the next button
                    bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                              '2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
                    time.sleep(2)
                    # adding random interests
                    random_value = randint(8, 12)
                    try:
                        for i in range(3, random_value):
                            bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div['
                                                      '2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/div[' +
                                                      str(randint(1, 8)) + ']/div[2]/div[' +
                                                      str(randint(1, 5)) + ']').click()
                            time.sleep(0.3)
                    except:
                        pass
                    time.sleep(0.5)
                    # pressing the next button
                    bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                              '2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
                    time.sleep(2)
                    # following some accounts
                    random_value = randint(4, 10)
                    try:
                        for i in range(1, random_value):
                            bot.find_element_by_xpath(
                                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                '2]/div[2]/div/div/div[3]/section/div/div/div/div[' + str(randint(3, 10)) +
                                ']/div/div/div/div[2]/div[1]/div[2]').click()
                    except:
                        pass
                    time.sleep(2)
                    # clicking the final follow button
                    bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                              '2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
                    time.sleep(2)
                    # clicking the skip for now button for the notifications
                    bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div['
                                              '2]/div/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div').click()
                    time.sleep(2)
                    flag = False
                    # and the account has been created
                    # clicking the cookie thing
                    bot.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]').click()
                    time.sleep(0.1)
                    username = bot.find_element_by_xpath(
                        '/html/body/div/div/div/div[2]/header/div/div/div/div[2]/div/div/div['
                        '2]/div/div[2]/div/span').text
                    # writing the credentials to a text file
                    f = open("accounts.txt", "a+")
                    f.write("Username: " + username + " || Email: " + email[0] + " || Password: " + password[0] + "\n")
                    f.close()
                    bot.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]').click()
                    time.sleep(2)
                except:
                    error_list.append(False)
                    bot.close()
        local_log_flag.append(True)
        bot.close()


if __name__ == '__main__':
    # creating different bots for different tasks
    # these 6 bots are creating the twitter account
    bot1 = Sign_Up_Bot()
    bot2 = Sign_Up_Bot()
    bot3 = Sign_Up_Bot()
    bot4 = Sign_Up_Bot()
    bot5 = Sign_Up_Bot()
    bot6 = Sign_Up_Bot()

    bot7 = Tweet_Bot()

    # multiprocessing used to create a tweeter account
    process1 = multiprocessing.Process(target=bot1.get_full_name, args=(full_name,))
    process2 = multiprocessing.Process(target=bot2.get_email, args=(email,))
    process3 = multiprocessing.Process(target=bot3.get_password, args=(password,))
    process4 = multiprocessing.Process(target=bot4.get_bio, args=(bio,))
    process6 = multiprocessing.Process(target=bot5.get_profile_picture, )
    process5 = multiprocessing.Process(target=bot6.create_twitter_account, args=(errors, log_flag))
    process7 = multiprocessing.Process(target=bot7.sign_in, args=(log_flag,))
    # starting all the processes
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    # joining all the processes
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()

# websites used for this autogenerated-twitter bot
# https://tempail.com/en/ temporary email address
# https://www.behindthename.com/random/ random name
# https://nordpass.com/password-generator/ random password
# https://sassycaptions.com/bio-generator/ generating bio
# https://twitter.com/explore twitter
# https://thispersondoesnotexist.com/image random face generator
# https://writingexercises.co.uk/random-images.php? random image generator
# https://inspirobot.me/ random inspirational image quotes
# https://randomwordgenerator.com/motivational-quote.php # inspirational quotes
# please note, that twitter might ask some of these accounts to fill a phone number
# THIS PROJECT IS NO LONGER BEING MAINTAINED
# TWITTER IS KNOWN FOR CHANGING A COUPLE OF THINGS IN THEIR WEBSITE, SO THIS MIGHT NOT WORK AT ALL
