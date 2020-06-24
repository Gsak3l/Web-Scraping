from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):  # constructor
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()  # opens Firefox browser

    def login(self):
        bot = self.bot
        bot.get('https://www.twitter.com/')  # we give the link of twitter to our bot
        time.sleep(5)  # sleep for 5 seconds

        bot.find_element_by_class_name('css-18t94o4.css-1dbjc4n.r-1niwhzg.r-11mg6pl.r-sdzlij.r-1phboty.'
                                       'r-rs99b7.r-18kxxzh.r-1q142lx.r-1w2pmg.r-1n0xq6e.r-1mnahxq.r-1vsu8ta.'
                                       'r-aj3cln.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr').click()  # click the cookie concern button

        bot.find_element_by_class_name('css-4rbku5.css-18t94o4.css-1dbjc4n.r-1niwhzg.'  # getting element by class name 
                                       'r-p1n3y5.r-sdzlij.r-1phboty.r-rs99b7.r-1loqt21.'
                                       'r-1w2pmg.r-1vsu8ta.r-aj3cln.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr').click()  # and clicking the element-button
        time.sleep(3)  # sleep for 3 seconds

        email = bot.find_element_by_name('session[username_or_email]')  # getting the username element by name
        password = bot.find_element_by_name('session[password]')  # getting the password element by name

        email.clear()  # emptying the email form just to be safe
        password.clear()  # emptying the password form just to be safe

        email.send_keys(self.username)  # adding the credentials
        password.send_keys(self.password)  # adding the credentials
        time.sleep(1)  # waiting 1 second after adding the credentials
        password.send_keys(Keys.RETURN)  # pressing enter instead of pressing the button
        time.sleep(3)  # waiting 3 seconds to load our home page

    def like_tweet(self, hashtag):  # function that likes tweets
        bot = self.bot
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
                        '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[4]/div/div/section/div/div/div/div['
                        + str(
                            counter) + ']/div/div/div/div/article/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/div/div[1]') \
                        .click()
                    counter += 1
                    time.sleep(1)
            except:
                pass


mikeBot = TwitterBot('quantina165@vteensp.com', 'fC#o$I7MQ8w&')
mikeBot.login()
time.sleep(3)
mikeBot.like_tweet('#spongebob')
