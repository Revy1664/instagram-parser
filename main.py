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
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div/label/input').send_keys('nmaksimov976@gmail.com')
    # Ввод пароля
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div/label/input').send_keys('Nik.2005')

    # Нажатие кноки "Войти"
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div[3]/button').click()

    # Нажатие кнопки "Не сейчас"
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()

    for i in range(21):

        for j in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML") # Получение содержимого html-тега
        
            soup = get_soup(html)
            links = get_src(soup)
        download_images(links)


def download_images(links):
    '''
    Эта функция скачивает изображения в папку img
    '''
    os.chdir('C:\\Users\\Никита\\Desktop\\instagram-parser\\img') # Переход в папку img


    # Скачивание каждого файла
    for i in range(len(links)):
        name = f'{i}.jpeg' # Имя файла
        url = links[i] # URL для скачивания файла
        urllib.request.urlretrieve(url, name) # Скачивание файла


def main():
    url = 'https://www.instagram.com/mashina_satam/?hl=ru'

    print(get_html(url))

if __name__ == '__main__':
    main()