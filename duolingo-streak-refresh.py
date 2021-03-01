import time
import selenium

from selenium import webdriver


class refresh_streak:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        preferences = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", preferences)
        self.bot = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)

    def refresh(self, email, password):
        flag = True
        while flag:
            try:
                duo = self.bot
                duo.get('https://www.duolingo.com/')
                # trying to click the 'I already have an account button'
                links = duo.find_elements_by_tag_name('a')
                for possible_buttons in links:
                    if possible_buttons.text == 'I ALREADY HAVE AN ACCOUNT':
                        possible_buttons.click()
                time.sleep(1)

                # typing the credentials in the input and pressing the login button
                inputs = duo.find_elements_by_tag_name('input')
                inputs[0].send_keys(email)
                inputs[1].send_keys(password)

                #  ----------- find a different way to make this work, classes are static ----------- #
                duo.find_element_by_class_name('_2oW4v').click()
                time.sleep(2)
                #  ----------- find a different way to make this work, classes are static ----------- #

                # buying the streak freeze
                duo.get('https://www.duolingo.com/shop')

                time.sleep(5)

                lis = duo.find_elements_by_tag_name('li')
                while len(lis) == 0:
                    lis = duo.find_elements_by_tag_name('li')

                for li in lis:
                    if 'Double or Nothing' in li.get_attribute('outerHTML'):
                        print('yeah')
                        li.find_element_by_tag_name('button').click()
                        flag = False
            except:
                pass


if __name__ == '__main__':
    bot = refresh_streak()
    bot.refresh('hahahaha@hahaha.go', 'hahahaha@hahaha.go')
