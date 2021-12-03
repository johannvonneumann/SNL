import pandas as pd
import os


# # .csv 파일을 한 개씩 열어서 Column 길이 검사. (index=False)가 빠져있는 경우를 검사하기 위함
# df = pd.DataFrame()
# for i in range(1, len(file_list) + 1):
#     df_temp = pd.read_csv(f'./crawling_data/reviews_2016_{i}.csv')
#     if len(df_temp.columns) != 2:
#         df_temp = pd.read_csv(f'./crawling_data/reviews_2016_{i}.csv', index_col=0)
#     df_temp.dropna(inplace=True)  # NaN 값 제거
#     df_temp.drop_duplicates()  # 추가 설명 필요
#     df_temp.columns = ['title', 'reviews']  # column 명 재설정
#     # df_temp.to_csv(f'./crawling_data/new_reviews_2016_{i}.csv', index=False)
#     df = pd.concat([df, df_temp], ignore_index=True)
#
# print(df.info())
# df.to_csv('./crawling_data/review_2016.csv', index=False)
# print(df)
# exit()



###########################################
# df = pd.read_csv('./crawling_data/reviews_2016_2.csv')      # index_col=0 을 주는 이유 -> .csv 파일에 인덱스가 포함되었을 경우 인덱스를 부여하지 않겠다는 것을 의미
# for i in range(2, 60):
#     df_temp = pd.read_csv(f'./crawling_data/reviews_2016_{i}.csv', index_col=0)
#     df_temp.dropna(inplace=True)        # NaN 값 제거
#     df_temp.drop_duplicates()           # 추가 설명 필요
#     df_temp.columns = ['title', 'reviews']      # column 명 재설정
#     df_temp.to_csv(f'./crawling_data/reviews_2016_{i}.csv', index=False)
#     df = pd.concat([df, df_temp], ignore_index=True)


def concatRawData(year):
    # crawling_data 폴더에 들어있는 .csv 파일의 갯수만큼 반복
    files = os.listdir('./crawling_data')
    file_list = []
    for i in range(len(files)):
        if files[i].endswith('.csv'):
            file_list.append(files[i])

    # .csv 파일을 한 개씩 열어서 Column 길이 검사. (index=False)가 빠져있는 경우를 검사하기 위함
    df = pd.DataFrame()
    for i in range(1, len(file_list) + 1):
        df_temp = pd.read_csv(f'./crawling_data/reviews_2016_{i}.csv')
        if len(df_temp.columns) != 2:
            df_temp = pd.read_csv(f'./crawling_data/reviews_2016_{i}.csv', index_col=0)
        df_temp.dropna(inplace=True)  # NaN 값 제거
        df_temp.drop_duplicates(inplace=True)   # 데이터 중복 제거
        df_temp.columns = ['title', 'reviews']  # column 명 재설정
        df_temp.to_csv(f'./crawling_data/reviews_2016_{i}.csv', index=False)
        df = pd.concat([df, df_temp], ignore_index=True)        # True 가 아니면 인덱스가 생기므로 주의

    df.to_csv(f'./crawling_data/review_{year}.csv', index=False)
    print(f'"review_{year}.csv" is saved.')


def concatMergedData():
    path = './crawling_data_year'
    df = pd.DataFrame()
    for i in range(15, 22):
        df_temp = pd.read_csv(f'{path}/reviews_20{i}.csv')
        df_temp.dropna(inplace=True)  # NaN 값 제거
        df_temp.drop_duplicates(inplace=True)  # 데이터 중복 제거
        df_temp.columns = ['title', 'reviews']  # column 명 재설정'title', 'reviews']
        df_temp.to_csv(f'{path}/reviews_20{i}.csv', index=False)
        df = pd.concat([df, df_temp], ignore_index=True)
    df.drop_duplicates(inplace=True)
    print(df.info())
    df.to_csv(f'{path}/reviews_2015_2021.csv', index=False)
    print(f'"reviews_2015_2021.csv" is saved.')


if __name__ == '__main__':
    # concatRawData(year='2016')
    concatMergedData()

