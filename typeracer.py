from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Bot:
    def __init__(self, WPM):
        self.driver = webdriver.Firefox()
        self.website = "https://play.typeracer.com/"
        self.full_text = ""
        self.WPM = WPM
        self.time = 2

    def retrieve_text(self):
        span = self.driver.find_elements_by_xpath("//span[@unselectable='on']")

        if len(span) == 2:
            self.full_text = span[0].text + " " + span[1].text
        else:
            self.full_text = span[0].text + span[1].text + " " + span[2].text
        print(len(self.full_text), self.full_text)

        if len(self.full_text) < 150:
            self.time = (len(self.full_text) / self.WPM) / 100 + 0.103
        elif len(self.full_text) < 220:
            self.time = (len(self.full_text) / self.WPM) / 100 + 0.099
        else:
            self.time = (len(self.full_text) / self.WPM) / 100 + 0.0916


def main():
    tp = Bot(WPM=100)
    tp.driver.get("https://play.typeracer.com?rt=2nieuhkl5iBV")
    sleep(5)
    tp.driver.find_element_by_class_name("qc-cmp-button").click()
    tp.driver.implicitly_wait(1)
    tp.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, Keys.ALT, 'K')
    sleep(1)
    # link = tp.driver.find_element_by_link_text("Enter a typing race").click()

    tp.retrieve_text()

    input_field = WebDriverWait(tp.driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.txtInput")))

    for letter in tp.full_text:
        input_field.send_keys(letter)
        sleep(tp.time)


if __name__ == "__main__":
    main()
