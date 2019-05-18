from urllib.request import urlopen
from bs4 import BeautifulSoup

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
