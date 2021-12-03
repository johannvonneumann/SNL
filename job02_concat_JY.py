import pandas as pd

# df = pd.read_csv('./crawling_data/reviews_2018_1.csv', index_col=0 ) 지우기

df = pd.DataFrame()
for i in range(1, 51):
    df_temp = pd.read_csv('./crawling_data/reviews_2018_{}.csv'.format(i))
    df_temp.dropna(inplace = True)
    df_temp.drop_duplicates()
    df_temp.columns = ['title', 'reviews']
    df_temp.to_csv('./crawling_data/reviews_2018_{}.csv'.format(i),
                     index=False)
    df = pd.concat([df, df_temp], ignore_index = True)
df.info()
df.to_csv('./crawling_data/reivews_2018.csv', index = False)

