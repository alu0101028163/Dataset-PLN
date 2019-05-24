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

# Es necesario tener instalado el webdriver de chrome
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
browser = webdriver.Chrome(executable_path='/home/hyydra/Desktop/chromedriver/chromedriver', chrome_options=option)

# Esta función obtiene los títulos de los libros de una categoría determinada dentro de un
# rango de páginas, teniendo en cuenta que la url a la que va acceder tiene la forma:
# "https://www.goodreads.com/shelf/show/" + category_name + "?page=" + page_number
def scrap_category(category_name, search_range):

    # Array que contiene los títulos de los libros
    book_names = []

    for i in range(search_range):

        quote_page = "https://www.goodreads.com/shelf/show/" + category_name + "?page=" + str(i + 1)
        # Obtenemos la página
        browser.get(quote_page)
        # Inicializamos Beautiful Soup
        soup = BeautifulSoup(browser.page_source,'lxml')
        # Buscamos dentro de la página todas aquellos elementos cuya clase corresponda con
        # bookTitle y obtenemos de ellos el nombre del libro.
        names = soup.find_all('a', attrs={"class":'bookTitle'})
        # Lo que nos va a devolver son links, así que para cada uno de esos links tomamos
        # su texto y lo guardamos. También eliminamos todas las comillas que encontremos en los
        # títulos para evitar que Weka falle.
        for name in names:
                book_name = name.text
                book_name = re.sub(r'\"','',book_name)
                book_names.append(book_name)

    return book_names

# Este método guarda cierta categoría y sus libros en un fichero
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



# ------------------------------------------------------------------------------
# ---------------------------- INICIO DEL PROGRAMA -----------------------------
# ------------------------------------------------------------------------------

# Si no se introduce el número correcto de argumentos se muestra el uso del programa
# y se lanza error.
if ((len(sys.argv) < 3)) or (sys.argv[1] not in ('-a','--automatic')):
    print_usage()
    exit()

book_names = []

# El primer argumento es el modo de uso
if(sys.argv[1] in ('-a','--automatic') ):

    file_name = sys.argv[2]             # El segundo argumento es el nombre del fichero
    maxpages  = sys.argv[3]             # El tercer argumento es el rango de páginas
    file_ = open(file_name,'r')

    # Aquí pondrías una ruta a las credenciales que necesitas para loguearte
    # dentro de goodreads.com, si no te logueas no puedes pasar de una página por
    # género.
    credentials = open("/home/hyydra/Desktop/credentials.txt")
    user_email = credentials.readline().split()
    user_password = credentials.readline().split()
    credentials.close()

    # Nos logueamos en la página de goodreads
    browser.get ("https://www.goodreads.com/user/sign_in")

    browser.find_element_by_id("user_email").send_keys(user_email)
    browser.find_element_by_id("user_password").send_keys(user_password)
    browser.find_element_by_name("next").click()

    # En un fichero guardamos las categorías que queremos obtener
    categories = []
    for line in file_:
        categories.append(line.strip())

    # Para cada categoría rascas los datos
    for category in categories:
        book_names = scrap_category(category,int(maxpages))
        category_to_file(("../outputs/" + category + ".txt"), category, book_names)
