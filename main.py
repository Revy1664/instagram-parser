from bs4 import BeautifulSoup as BS
from selenium import webdriver
from time import sleep
import urllib
from urllib.request import urlretrieve
import os

def get_soup(html):
    '''
    Эта функция возращает объект soup'a
    '''

    soup = BS(html, 'lxml')
    
    return soup 

def get_src(soup):
    '''
    Эта функция возращает ссылки на изображения
    '''
    items = soup.find_all('div', class_="KL4Bh") # Поиск блоков с изображениями
    
    links = []

    for item in items: # Проход по блокам и поиск тегов img
        link = item.find('img').get('src') # Извлечение ссылок из тега img
        links.append(link)

    return links

def get_html(url):
    '''
    Эта функция возращает содержимое html-тега
    '''
    driver = webdriver.Chrome() # Настройка WebDriver
    driver.get(url) # Переход по URL

    # Вход
    driver.find_element_by_class_name('_9AhH0').click()
    driver.implicitly_wait(50)
    # Ввод логина
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div/label/input').send_keys('steinsgate95@mail.ru')
    # Ввод пароля
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div/label/input').send_keys('gQ25yz7832')

    # Нажатие кноки "Войти"
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div[3]/button').click()

    # Нажатие кнопки "Не сейчас"
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()

    # Скролл до самого низа страницы с получением ссылок на все посты
    for i in range(0, 64):
        driver.execute_script(f"window.scrollTo({768 * i}, {768 * (0 + i)})") 
        sleep(2)
        
        
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML") # Получение содержимого html-тега

        soup = get_soup(html)
        links = get_src(soup)

        # Запись ссылок в файл
        for j in links:
            with open('links.txt', 'a') as file:
                file.write(f'{j}\n')

def download_images(links):
    '''
    Эта функция скачивает изображения в папку img
    '''
    os.chdir('C:\\Users\\Никита\\Desktop\\instagram-parser\\img') # Переход в папку img

    # Открытие файла с номером изображения
    infile = open('count.txt', 'r')
    count = int(infile.read())
    infile.close()

    # Скачивание каждого файла
    for link in links:
        name = f'{count}.jpg'
        url = link
        urllib.request.urlretrieve(url, name) # Скачивание файла
        count += 1

        # Запись нового значения в файл
        outfile = open('count.txt', 'w')
        outfile.write(str(count))
        outfile.close()
       
def main():
    url = 'https://www.instagram.com/mashina_satam/?hl=ru'

    get_html(url)
    
    # Получение всех ссылок
    infile = open('links.txt', 'r')
    text = infile.read()

    # Поиск и удаление дубликатов
    rows = text.splitlines()
    unique_rows = list(dict.fromkeys(rows))
    infile.close()

    # Запись уникальных ссылок в файл
    outfile = open('links.txt', 'w')
    for i in unique_rows:
        outfile.write(i + '\n')
    outfile.close()

    # Чтение ссылок из файла
    infile = open('links.txt', 'r')
    links = infile.readlines()
    infile.close()

    download_images(links)

if __name__ == '__main__':
    main()