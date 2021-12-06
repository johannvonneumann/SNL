import pandas as pd

df = pd.read_csv('./crawling_data_year/reviews_2015_2021.csv')
one_sentences = []
for title in df['title'].unique():
    temp = df[df['title'] == title]
    temp = temp['reviews']
    one_sentence = ' '.join(temp)          # 문자열 붙이기
    one_sentences.append(one_sentence)
df_one_sentences = pd.DataFrame({'title': df['title'].unique(), 'reviews': one_sentences})
print(df_one_sentences.head())
df_one_sentences.to_csv('./crawling_data_year/naver_movie_reviews_onesentence_2015_2021.csv', index=False)


