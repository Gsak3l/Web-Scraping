import multiprocessing
import time
import random
import validators

from selenium import webdriver


def check_info(c_username, c_password, c_instagram_post_url):
    # username stuff
    c_username = input("username: ")
    while not validators.url("https://www.instagram.com/" + str(c_username) + "/"):
        c_username = input("incorrect username, try again: ")
    u_flag = False
    # password stuff
    c_password = input("password: ")
    while not len(c_password) > 6:
        input("incorrect password will not work, try again: ")
    # instagram post stuff
    c_instagram_post_url = input("post url: ")
    while not validators.url("https://www.instagram.com/" + str(c_instagram_post_url) + "/"):
        c_instagram_post_url = input("this doesn't seem right, try again: ")


if __name__ == '__main__':
    username = password = instagram_post_url = ''
    check_info(username, password, instagram_post_url)
    # comment_spammer = webdriver.Chrome(executable_path='./chromedriver')
    # comment_spammer.get(instagram_post_url)
    print(username, password, instagram_post_url)
