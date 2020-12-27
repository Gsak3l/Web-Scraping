import multiprocessing
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
        input("incorrect password will not work, try again: ")
    # instagram post stuff
    credentials_2[2] = input("post url: ")
    while not validators.url("https://www.instagram.com/" + str(credentials_2[2]) + "/"):
        credentials_2[2] = input("this doesn't seem right, try again: ")
    return credentials_2


def comment(credentials_2):
    comment_spammer = webdriver.Chrome(executable_path='./chromedriver')
    comment_spammer.get(credentials_2[2])  # reaching the post
    # loggin in
    flag = True
    while flag:
        try:
            comment_spammer.find_elements_by_tag_name('input')[0].clear()
            comment_spammer.find_elements_by_tag_name('input')[1].clear()
            comment_spammer.find_elements_by_tag_name('input')[0].send_keys(credentials_2[0])
            comment_spammer.find_elements_by_tag_name('input')[1].send_keys(credentials_2[1])
            flag = False
        except:
            pass
    comment_spammer.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div[3]/button').click()
    time.sleep(15)


if __name__ == '__main__':
    credentials = check_info()
    comment(credentials)
    # comment_spammer = webdriver.Chrome(executable_path='./chromedriver')
    # comment_spammer.get(instagram_post_url)
