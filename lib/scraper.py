from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re

def scrap_category(category_name, search_range):

    book_names = []

    for i in range(search_range):
        quote_page = "https://www.goodreads.com/shelf/show/" + category_name + "?page=" + str(i + 1)
        page = urlopen(quote_page)
        soup = BeautifulSoup(page,'lxml')
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
    usage += "$python3 -a --automatic fileName "
    usage += "#it automatically scraps all the data of the categories passed in a file.\n"
    usage += "$python3 -m --manual categorie maxpages "
    usage += "#it automatically scraps all the \"maxpages\" pages of data of the category passed as an argument."
    print(usage)

if ((len(sys.argv) < 2)) or (sys.argv[1] not in ('-a','--automatic','-m','--manual')):
    print_usage()
    exit()

book_names = []

if(sys.argv[1] in ('-a','--automatic') ):
    if(len(sys.argv) < 3):
        print_usage()
        exit()

    file_name = sys.argv[2]
    file_ = open(file_name,'r')

    categories = []
    for line in file_:
        categories.append(line.strip())

    for category in categories:
        book_names = scrap_category(category, 1)
        category_to_file(("../outputs/" + category + ".txt"), category, book_names)
        print(book_names)



#
# for i in range(2):
#     quote_page = "https://www.goodreads.com/shelf/show/art?page=" + str(i + 1)
#     page = urlopen(quote_page)
#     soup = BeautifulSoup(page,'lxml')
#     names = soup.find_all('a', attrs={"class":'bookTitle'})
#
#     for name in names:
#             book_names.append(name.text)
#             # print(name.text)
#
# print(len(book_names))
