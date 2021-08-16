import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from time import sleep

def get_data(url):
	HEADERS = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6',
		'cache-control': 'max-age=0'
	}
	driver = webdriver.Chrome()
	driver.get(url)
	html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

	soup = BS(html, 'lxml')
	items = soup.find_all('div', class_="KL4Bh")
	links = []
	for item in items:
		item.find('img', class_="FFVAD")
		links.append(item)

	return links

def main():
	url = 'https://www.instagram.com/mashina_satam/?hl=ru'
	print(get_data(url))

if __name__ == '__main__':
	main()