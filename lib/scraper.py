from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import sys
import requests
import re


option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
browser = webdriver.Chrome(executable_path='/home/hyydra/Desktop/chromedriver/chromedriver', chrome_options=option)


def scrap_category(category_name, search_range):

    book_names = []

    for i in range(search_range):

        quote_page = "https://www.goodreads.com/shelf/show/" + category_name + "?page=" + str(i + 1)
        browser.get(quote_page)
        soup = BeautifulSoup(browser.page_source,'lxml')
        names = soup.find_all('a', attrs={"class":'bookTitle'})
        for name in names:
                book_name = name.text
                book_name = re.sub(r'\"','',book_name)
                book_names.append(book_name)

    return book_names

def category_to_file(file_name, category_name, books):
    file_ = open(file_name,'w+')
    for book in books:
        file_.write("\"" + book + "\"," + category_name + "\n")
    file_.close()

def print_usage():
    usage = "The usage of the application is: \n"
    usage += "$python3 -a --automatic fileName maxpages"
    usage += "#it automatically scraps all the data of the categories passed in a file."
    print(usage)

if ((len(sys.argv) < 3)) or (sys.argv[1] not in ('-a','--automatic')):
    print_usage()
    exit()

book_names = []

if(sys.argv[1] in ('-a','--automatic') ):

    file_name = sys.argv[2]
    maxpages  = sys.argv[3]
    file_ = open(file_name,'r')


    credentials = open("/home/hyydra/Desktop/credentials.txt")
    user_email = credentials.readline().split()
    user_password = credentials.readline().split()
    credentials.close()

    browser.get ("https://www.goodreads.com/user/sign_in")

    browser.find_element_by_id("user_email").send_keys(user_email)
    browser.find_element_by_id("user_password").send_keys(user_password)
    browser.find_element_by_name("next").click()

    categories = []
    for line in file_:
        categories.append(line.strip())

    for category in categories:
        book_names = scrap_category(category,int(maxpages))
        category_to_file(("../outputs/" + category + ".txt"), category, book_names)
