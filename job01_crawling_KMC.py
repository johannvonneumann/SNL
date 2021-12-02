from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


options = webdriver.ChromeOptions()
# options.add_argument('headless')        # Web-browser가 뜨지 않는다.
options.add_argument('lang=ko_KR')
options.add_argument('disable_gpu')

driver = webdriver.Chrome('./chromedriver', options=options)

review_button_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a/em'
review_number_xpath = '//*[@id="reviewTab"]/div/div/div[2]/span/em'
try:
    for i in range(1, 38):
        titles = []
        reviews = []
        url = f'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page={i}'
        for j in range(1, 21):
            print(j+((i - 1) * 20), '번째 영화 크롤링 중')
            try:
                driver.get(url)
                movie_title_xpath = f'//*[@id="old_content"]/ul/li[{j}]/a'
                title = driver.find_element_by_xpath(movie_title_xpath).text
                driver.find_element_by_xpath(movie_title_xpath).click()
                driver.find_element_by_xpath(review_button_xpath).click()
                review_range = int(driver.find_element_by_xpath(review_number_xpath).text.replace(',', '')) // 10 + 2
                if review_range > 6:
                    review_range = 6
                for k in range(1, review_range):
                    review_page_url = driver.find_element_by_xpath('//*[@id="movieEndTabMenu"]/li[6]/a').get_attribute('href')
                    driver.get(review_page_url + f'&page={k}')
                    for l in range(1, 11):
                        review_title_xpath = f'//*[@id="reviewTab"]/div/div/ul/li[{l}]/a/strong'
                        try:
                            driver.find_element_by_xpath(review_title_xpath).click()
                            time.sleep(0.3)
                            review = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div[1]/div[4]').text
                            # print('===================== =====================')
                            # print(title)
                            # print(review)
                            titles.append(title)
                            reviews.append(review)
                            driver.back()
                        except:
                            # print(f'{l}번째 Review가 없습니다.')
                            # driver.get(url)
                            break
            except Exception as E:
                print('error', E)
        df_review_20 = pd.DataFrame({'title': titles, 'reviews': reviews})
        df_review_20.to_csv(f'./crawling_data/reviews_{2020}_{i}.csv', index=False)
except Exception as E:
    print('totally error', E)
finally:
    driver.close()

# df_review = pd.DataFrame({'title': titles, 'reviews': reviews})
# df_review.to_csv(f'./crawling_data/reviews_{2020}.csv')