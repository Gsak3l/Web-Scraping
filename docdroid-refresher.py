import time

from selenium import webdriver
import multiprocessing


class doc_refresher:
    def __init__(self):
        self.bot = webdriver.Firefox()

    def refresh_teacher_pdf(self):
        bot = self.bot
        bot.get('https://greekbooks.netlify.app/professor-books.html')
        books = bot.find_elements_by_tag_name('li')
        for book in books:
            book.click()
            time.sleep(2)
        bot.close()

    def refresh_student_pdf_1(self):
        bot = self.bot
        bot.get('https://greekbooks.netlify.app/student-books.html')
        book_categories = bot.find_elements_by_tag_name('ul')
        for i in range(3):
            books = book_categories[i].find_elements_by_tag_name('li')
            for book in books:
                book.click()
                time.sleep(2)
        bot.close()

    def refresh_student_pdf_2(self):
        bot = self.bot
        bot.get('https://greekbooks.netlify.app/student-books.html')
        book_categories = bot.find_elements_by_tag_name('ul')
        for i in range(3, 6):
            books = book_categories[i].find_elements_by_tag_name('li')
            for book in books:
                book.click()
                time.sleep(2)
        bot.close()


if __name__ == '__main__':
    bot1 = doc_refresher()
    bot2 = doc_refresher()
    bot3 = doc_refresher()
    process1 = multiprocessing.Process(target=bot1.refresh_teacher_pdf, )
    process2 = multiprocessing.Process(target=bot2.refresh_student_pdf_1, )
    process3 = multiprocessing.Process(target=bot3.refresh_student_pdf_2, )
    process1.start()
    process2.start()
    process3.start()
    process1.join()
    process2.join()
    process3.join()
