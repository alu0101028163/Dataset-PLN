from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

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


for i in range(2):
    quote_page = "https://www.goodreads.com/shelf/show/art?page=" + str(i + 1)
    page = urlopen(quote_page)
    soup = BeautifulSoup(page,'lxml')
    names = soup.find_all('a', attrs={"class":'bookTitle'})

    for name in names:
            book_names.append(name.text)
            # print(name.text)

print(len(book_names))


# names = soup.find('div',attrs={'class','p13n-sc-truncate p13n-sc-line-clamp-1'})
# names = names.text.strip()
# print(names)
