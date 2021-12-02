from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('lang=ko_KR')
options.add_argument('disable_gpu')

driver = webdriver.Chrome('./chromedriver', options=options)


# https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page=1
# https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page=2
# 영화제목 xpath
# //*[@id="old_content"]/ul/li[1]/a
# //*[@id="old_content"]/ul/li[2]/a
# //*[@id="movieEndTabMenu"]/li[6]/a/em 리뷰버튼 버튼
#  //*[@id="reviewTab"]/div/div/div[2]/span 리뷰건수
# //*[@id="pagerTagAnchor1"]/span 리뷰페이지 버튼
# //*[@id="reviewTab"]/div/div/ul/li[1]/a/strong 리뷰제목
# //*[@id="content"]/div[1]/div[4]/div[1]/div[4] #class:user_tx
## //*[@id="movieEndTabMenu"]/li[6]/a
review_number_xpath = '//*[@id="reviewTab"]/div/div/div[2]/span/em'
review_button_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a'
try:
    for i in range(22,38):
        url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page={}'.format(i)
        titles = []
        reviews = []

        for j in range(1, 21):
            print(j+((i-1)*20),'번째 영화 크롤링 중')
            try:
                driver.get(url)
                movie_title_xpath = '//*[@id="old_content"]/ul/li[{}]/a'.format(j)
                title = driver.find_element_by_xpath(movie_title_xpath).text
                driver.find_element_by_xpath(movie_title_xpath).click()
                review_page_url = driver.find_element_by_xpath(review_button_xpath).get_attribute('href')
                ####
                driver.get(review_page_url)
                review_range = driver.find_element_by_xpath(review_number_xpath).text.replace(',','')
                review_range = int(review_range)
                review_range = review_range //10 +2
                if review_range > 6: review_range = 6
                for k in range(1,review_range):

                    driver.get(review_page_url + '&page={}'.format(k))
                    time.sleep(1)
                    for l in range(1,11):
                       review_title_xpath='//*[@id="reviewTab"]/div/div/ul/li[{}]/a/strong'. format(l)
                       try:
                           driver.find_element_by_xpath(review_title_xpath).click()
                           time.sleep(1)
                           review = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div[4]').text
                           # print('===============================================================================')
                           # print(title)
                           # print(review)  ###항상 추가 된다
                           titles.append(title)
                           reviews.append(review)
                           driver.back()
                       except:
                           driver.get(url)
                           break

            except:
                 print('error')
        df_review_20 = pd.DataFrame({'title':titles,'reviews':reviews})
        df_review_20.to_csv('./crawling_data/reviews_{}_{}.csv'.format(2020,i) index=False)
except:
    print('totally error')
finally:
    driver.close()
# df_review = pd.DataFrame({'title':titles,'reviews':reviews})
# dr_review.to_csv('./crawling_data/reviews_{}'.format(2020))
