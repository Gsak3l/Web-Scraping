import multiprocessing
import time
import random
from selenium import webdriver

if __name__ == '__main__':
    flag = True
    while flag:
        username = input("username: ")

        password = input("password: ")
        instagram_post_url = input("instagram post url: ")


    # driver
    comment_spammer = webdriver.Chrome(executable_path='./chromedriver')
    comment_spammer.get(instagram_post_url)

