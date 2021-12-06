from datetime import datetime
from gensim.models import Word2Vec
import pandas as pd
import time


review_word = pd.read_csv('./crawling_data_year/cleaned_review_2015_2021.csv')
review_word.info()

# 약 4000 여개의 형태소들을 가방에 담는다. -> BOW(Bag Of Words)
# 가방에는 형태소들이 관계성이나 순서에 상관없이 들어있다.
# 이 가방을 Word2Vec 모델에 전달하여 형태소들의 의미에 벡터를 부여한다.
# 벡터가 부여되면 자연스럽게 형태소들이 군집화를 이루게 된다.
# 각 단어의 축을 생성하고 해당 단어와 관계있는 단어는 가까이 배치되고
# 관계 없는 단어는 상대적으로 멀리 배치된다.
# 즉, 단어에 차원이 부여되며 이를 벡터라이징(Vectorizing)이라 한다.

# review_word 에서 'cleaned_sentences' 컬럼만 리스트로 parsing 하여 사용한다.
# BOW(Bag Of Words)를 만드는 과정.
start_time = time.time()            # Runtime 계산을 위한 임시 선언
cleaned_token_review = list(review_word['cleaned_sentences'])
cleaned_tokens = []
for sentence in cleaned_token_review:
    # 띄어쓰기를 기준으로 잘라내고 cleaned_tokens 에 추가한다.
    token = sentence.split()
    # cleaned_tokens.append(token)은 2차원이 되기 때문에 1차원으로 구성하기 위해서는 아래의 방법을 사용한다.
    cleaned_tokens.append(token)
print(cleaned_tokens[-20:])
print(len(cleaned_tokens))
print(f'runtime is {time.time() - start_time:.4f} seconds')

# 임베딩 모델 구성
# vector_size:100   100차원의 벡터 스페이스를 구성한다. 모든 단어는 100차원으로 축소시킨다.
# window=4          4개 단어씩 학습을 한다.
# "동해 물 백두산 마르고 닳도록 하느님 보우하사 우리 나라 만세"를 예시로 하면
# 동해 물 백두산 마르고 학습.
# 물 백두산 마르고 닭도록 학습.
# min_count=20      등장 횟수가 20회 이하인 단어는 무시한다.
# workers=6         CPU 코어 갯수를 입력하면 된다. (최대 사용)
# epochs=100        학습은 100번 진행한다.
# sg=1              Skip-Gram 의 약자. 모델 학습 방법인데 정확한 것은 잘 모름.
start_time = time.time()            # Runtime 계산을 위한 임시 선언
# embedding_model = Word2Vec(cleaned_tokens, vector_size=100, window=4, min_count=20, workers=6, epochs=100, sg=1)
embedding_model = Word2Vec(cleaned_tokens, size=100, window=4, min_count=20, workers=6, iter=100, sg=1)
embedding_model.save(f'./models/word2VecModel_2015_2021_{datetime.now().strftime("%y%m%d-%H%M%S")}.model')
# gensim 4.0.0 미만의 경우 아래 방식으로 출력해야한다.
print(embedding_model.wv.vocab.keys())
print(len(embedding_model.wv.vocab.keys()))
# gensim 4.0.0 이상의 경우 아래 방식으로 출력해야한다.
# print(list(embedding_model.wv.index_to_key))
# print(len(list(embedding_model.wv.index_to_key)))
print(f'runtime is {time.time() - start_time:.4f} seconds')
