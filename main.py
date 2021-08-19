import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from time import sleep
import urllib
from urllib.request import urlretrieve
import os

def get_data(url):
    # Добавление заголовков
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6',
        'cache-control': 'max-age=0'
    }

    # Настройка ChromeDriver и переход по url
    driver = webdriver.Chrome()
    driver.get(url)

    # Вход
    # Нажатие на пост
    driver.find_element_by_class_name('_9AhH0').click()
    driver.implicitly_wait(10)
    # Ввод логина
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div[1]/div/label/input').send_keys('steinsgate95@mail.ru')
    # Ввод пароля
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div[2]/div/label/input').send_keys('gQ25yz7832')

    # Нажатие кноки "Войти"
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/div/div/div[1]/div/form/div[1]/div[3]/button').click()

    # Нажатие кнопки "Не сейчас"
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()


    # Имитация скролла
    for i in range(37):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1.5)

    # Получение содержимого тега html
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

    # Парсинг
    soup = BS(html, 'lxml')
    items = soup.find_all('div', class_="KL4Bh")
    links = []
    for item in items:
        image = item.find('img', class_="FFVAD")
        links.append(image.attrs['src'])

    # Скачивание файлов
    # os.chdir('C:\\Users\\Никита\\Desktop\\instagram-parser\\img')
    # for i in range(447):
    #     name = f'img{i}.png'
    #     url = links[i]
    #     urllib.request.urlretrieve(url, name)


    return links

def main():
    url = 'https://www.instagram.com/mashina_satam/?hl=ru'
    print(*get_data(url), sep='\n')

if __name__ == '__main__':
    main()