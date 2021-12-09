from konlpy.tag import Okt
import pandas as pd
import re

# 동일한 제목(title)을 가진 리뷰를 하나로 묶어버린 onesentence.csv 파일을 불러온다.
# onesentence.csv는 job03 에서 생성하였다.
df = pd.read_csv('./crawling_data_year/naver_movie_reviews_onesentence_2015_2021.csv')
print(df.head())
df.info()

# df2 = pd.read_csv('./crawling_data_year/naver_movie_reviews_onesentence_2015_2021.csv')
# print(df2.head())
# df2.info()
#
# stopwords = pd.read_csv('./stopwords.csv', index_col=0)
# cleaned_sentences = []
# for cleaned_sentence in df2.cleaned_sentences:
#     cleaned_sentence_words = cleaned_sentence.split()
#     words = []
#     for word in cleaned_sentence_words:
#         if word not in list(stopwords):
#             words.append(word)
#     cleaned_sentence = ' '.join(words)
#     cleaned_sentences.append(cleaned_sentence)
# df2['cleaned_sentences'] = cleaned_sentences
# df2.to_csv('./stopwords.csv', index=False)
# exit()
okt = Okt()

stopwords = pd.read_csv('./stopwords.csv', index_col=0)
# print(df.loc[0, 'reviews'])
# setence = re.sub('[^가-힣 ]', ' ', df.loc[0, 'reviews'])
# print(setence)
# token = okt.pos(setence, stem=True)
# print(token)

count = 0
cleaned_sentences = []
for sentence in df['reviews']:
    count += 1
    if count % 10 == 0:
        print('.', end='')
    if count % 100 == 0:
        print()
    sentence = re.sub('[^가-힣 ]', '', sentence)       # 단어 지우기
    token = okt.pos(sentence, stem=True)            # stem=True, 어간의 원형으로 변환해줌. 먹어 -> 먹다
    df_token = pd.DataFrame(token, columns=['word', 'class'])
    df_cleaned_token = df_token[(df_token['class'] == 'Noun') |
                                (df_token['class'] == 'Verb') |
                                (df_token['class'] == 'Adjective')]
    words = []
    for word in df_cleaned_token['word']:
        if len(word) > 1:
            if word not in list(stopwords['stopword']):
                words.append(word)
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)
df['cleaned_sentences'] = cleaned_sentences
print(df.info())
df = df[['titles', 'clean_sentences']]
df.to_csv('./cleaned_review_2015_2011.csv')
