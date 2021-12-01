from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


options = webdriver.ChromeOptions()
# options.add_argument('headless')    # Web-browser가 열리지 않게 해주는 설정
options.add_argument('lang=ko_KR')
options.add_argument('disable_gpu')

driver = webdriver.Chrome('./chromedriver', options=options)

titles = []
reviews = []

for page_number in range(1, 38):
    url = f'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page={page_number}'
    driver.get(url)
    for title_number in range(1, 21):
        try:
            movie_title_xpath = f'//*[@id="old_content"]/ul/li[{title_number}]/a'
            title = driver.find_element_by_xpath(movie_title_xpath).text
            print(title)
        except Exception as E:
            print(f'Unknown error occurred..\nError: {E}')
    print(len(title))
