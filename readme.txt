# Crawling 작업

# Crawling은 각자 진행하고 빨리 완성되는 코드로 연도를 나눠서 진행하겠습니다.
# 일단 2020년 개봉작만 크롤링 해주시고 저장 형식은 csv로 하겠습니다.
# 나머지는 연도별로 나눠서 크롤링 해서 합칠게요.
# 컬럼명은 ['title', 'reviews']로 통일해주세요.
# 파일명은 reviews_0000.csv로 해주세요. 0000은 해당 연도입니다.
# 크롤링한 데이터 파일은 아래 링크로 올려주세요.
# https://drive.google.com/drive/folders/1vICarPIiRxa65pItqwBEwvMD_tlf0xQw?usp=sharing

# 2021-12-02 Reminder
# 한 사람당 1년치 분량만 Crawling 해주시면 되겠습니다.
# 김민철 - 2016년
# 서보권 - 2017년
# 이주연 - 2018년
# 조은호 - 2019년
# 황현하 - 2021년
# 위에서 명시한 연도를 확인하시고, 해당 년도의 영화 타이틀과 리뷰를 크롤링하시면 되겠습니다.
# 크롤링 한 데이터(.csv)는 아래 URL에 업로드 부탁드립니다.
# https://drive.google.com/drive/folders/1JprpPHRpmA4rdd115VRnbp_42c5Vsofw
# 더 이상 혼나기 싫어요.. ㅠ

# 2021-12-02  17:20 추가
# 리뷰를 가져오는 과정에서 '리뷰 버튼'의 xpath 에 대한 이슈가 있습니다.
# 예시 1: https://movie.naver.com/movie/bi/mi/basic.naver?code=141789
# 예시 2: https://movie.naver.com/movie/bi/mi/basic.naver?code=145739
# 예시 1번의 경우 저희가 작성한 //*[@id="movieEndTabMenu"]/li[6]/a/em 스크립트가 유효합니다.
# 예시 2번의 경우 //*[@id="movieEndTabMenu"]/li[5]/a/em 가 되어 비정상적인 접근을 하게됩니다.
# 즉, 리뷰가 아니라 다른 경로로 접근하여 크롤링을 진행하려다 보니 에러가 발생합니다.
# 이슈를 해결하기위해 코드 수정이 필요합니다. 이슈 해결을 위해 다같이 방법을 찾아봅시다.

# 2021-12-02  23:29 추가
# 트레이스백(Traceback)을 위한 에러 디버그 및 파일 출력 코드 추가
# 원하시는 경우, job01_crawling_KMC-1.py의 내용을 복사하여 본인이 작업하고 있던 .py에 붙여넣기 하시면 됩니다
# 113번 라인에서 crawlData()의 매개변수인 year에 본인이 크롤링해야하는 연도를 문자열형태로 적어주면 알아서 합니다.
