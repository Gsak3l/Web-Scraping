import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Auto_trading_bot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.bot = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)

    def do_stuff(self, email, password):
        duo = self.bot
        duo.get('https://www.duolingo.com/?isLoggingIn=true')
        duo.find_element_by_xpath('/html/body/div[1]/div/div/span[1]/div/div[1]/div[2]/div/div[2]/a').click()
        time.sleep(0.5)
        inputs = duo.find_elements_by_tag_name('input')
        inputs[0].send_keys(email)
        inputs[1].send_keys(password)
        duo.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/form/div[1]/button').click()
        time.sleep(7)
        duo.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[3]/div[2]/div[3]/a').click()
        time.sleep(2)
        for o in range(6, 2, -1):
            for z in range(10, 0, -1):
                duo.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div['
                                          + str(o) + ']/a[' + str(z) + ']').click()
                time.sleep(2)
                flag = True
                while flag:
                    duo.find_element_by_xpath('/html/body').send_keys(Keys.RETURN)
                    time.sleep(0.1)
                    duo.find_element_by_xpath('/html/body').send_keys(Keys.NUMPAD1)
                    time.sleep(0.1)
                    duo.find_element_by_xpath('/html/body').send_keys(Keys.NUMPAD2)
                    time.sleep(0.1)
                    duo.find_element_by_xpath('/html/body').send_keys(Keys.NUMPAD3)
                    time.sleep(0.1)
                    duo.find_element_by_xpath('/html/body').send_keys(Keys.NUMPAD4)
                    time.sleep(0.1)
                    try:
                        duo.find_element_by_class_name('_3Ri2U')
                        flag = False
                    except:
                        pass
                time.sleep(1)
                pairs = duo.find_elements_by_class_name('_3Y3Px')
                print(pairs)
                for x in range(2):
                    for i in range(len(pairs)):
                        try:
                            pairs[i].click()
                            for j in range(len(pairs)):
                                if i != j:
                                    try:
                                        pairs[j].click()
                                    except:
                                        pass
                        except:
                            pass
                time.sleep(1)
                flag2 = True
                while flag2:
                    try:
                        duo.find_element_by_xpath(
                            '/html/body/div[1]/div/div/div/div/div[3]/div/div[2]/div/button/span').click()
                        flag2 = False
                        time.sleep(1)
                    except:
                        pass
                flag2 = True
                while flag2:
                    try:
                        duo.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div/div/button').click()
                        flag2 = False
                        time.sleep(1)
                    except:
                        pass
                flag2 = True
                while flag2:
                    try:
                        duo.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div/div/button').click()
                        flag2 = False
                    except:
                        pass
                time.sleep(2)


if __name__ == '__main__':
    duo_bot = Auto_trading_bot()
    duo_bot.do_stuff('username goes here', 'password goes here')
