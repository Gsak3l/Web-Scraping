import time
import random
import validators

from selenium import webdriver


def check_info():
    credentials_2 = [''] * 3
    # username stuff
    credentials_2[0] = input("username: ")
    while not validators.url("https://www.instagram.com/" + str(credentials_2[0]) + "/") or not len(credentials_2[0]) >= 3:
        credentials_2[0] = input("incorrect username, try again: ")
    u_flag = False

    # password stuff
    credentials_2[1] = input("password: ")
    while not len(credentials_2[1]) > 6:
        credentials_2[1] = input("incorrect password will not work, try again: ")

    # instagram post stuff
    credentials_2[2] = input("post url: ")
    while not validators.url("https://www.instagram.com/" + str(credentials_2[2]) + "/"):
        credentials_2[2] = input("this doesn't seem right, try again: ")
    return credentials_2


def login(logger, credentials_2):
    # cookie button
    flag = True
    while flag:
        buttons = logger.find_elements_by_tag_name('button')
        try:
            for buttons in buttons:
                if buttons.text == 'Accept':
                    buttons.click()
                    flag = False
        except:
            pass

    # logging in
    flag = True
    while flag:
        try:
            logger.find_elements_by_tag_name('input')[0].clear()
            logger.find_elements_by_tag_name('input')[1].clear()
            logger.find_elements_by_tag_name('input')[0].send_keys(credentials_2[0])
            logger.find_elements_by_tag_name('input')[1].send_keys(credentials_2[1])
            flag = False
        except:
            pass
    logger.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[3]/button').click()

    # bypassing the save credentials step<
    while not flag:
        buttons = logger.find_elements_by_tag_name('button')
        for button in buttons:
            try:
                if button.text == 'Not Now':
                    button.click()
                    flag = True
            except:
                pass


def get_follower_names(follower_names_getter, credentials_2):
    names_2 = []
    follower_names_getter.get('https://www.instagram.com/' + str(credentials_2[0]))
    # getting the number of followers
    number_of_followers = follower_names_getter.find_elements_by_tag_name('li')[1].find_element_by_tag_name('span').text
    follower_names_getter.find_elements_by_tag_name('li')[1].click()
    time.sleep(1)

    follower_window = follower_names_getter.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
    lis = []

    while int(number_of_followers) - 1 >= len(lis):
        follower_names_getter.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', follower_window)
        lis = follower_names_getter.find_element_by_xpath('/html/body/div[5]/div/div/div[2]').find_elements_by_tag_name('li')

    for li in lis:
        try:
            if li.find_element_by_tag_name('span').text != '':
                names_2.append(li.find_element_by_tag_name('span').text)
        except:
            pass

    return names_2


def commenter(spammer, credentials_2, names_2):
    spammer.get(credentials_2[2])
    time.sleep(2)

    spammer.find_element_by_tag_name('textarea').click()

    buttons = spammer.find_elements_by_tag_name('button')

    flag = True
    while flag:
        for i in range(2):
            try:
                spammer.find_element_by_tag_name('textarea').send_keys('@' + names_2[random.randint(0, len(names_2) - 1)] + ' ')
            except:
                pass
        time.sleep(1)
        try:
            for button in buttons:
                if button.text == 'Post':
                    button.click()
        except:
            pass
        time.sleep(5)


def manager(credentials_2):
    bot = webdriver.Chrome(executable_path='./chromedriver')
    bot.get("https://www.instagram.com/accounts/login/")

    login(bot, credentials_2)
    names = get_follower_names(bot, credentials_2)
    commenter(bot, credentials_2, names)


if __name__ == '__main__':
    credentials = check_info()
    manager(credentials)
