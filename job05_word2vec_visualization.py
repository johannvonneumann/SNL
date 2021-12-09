# word2vec.py 에서 생성한 Word2VecModel_2015_2021.model 은 100차원이라서 시각화가 어렵다.
# 따라서 2차원으로 차원축소 후 시각화를 하여 데이터의 형태를 확인해보고자 한다.
import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE       # 시각화 패키지
from matplotlib import font_manager, rc
import matplotlib as mpl

# 한글 폰트 적용을 위한 폰트 불러오기
font_path = './malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
mpl.rcParams['axes.unicode_minus']=False
rc('font', family=font_name)

# 모델 불러오기
embedding_model = Word2Vec.load('./models/word2VecModel_2015_2021.model')
# 단어 하나를 테스트 해보고자 함
key_word = '일요일'
# most_similar 에 단어 하나를 주고, 제일 비슷한 10개를 출력해보고자 한다.
sim_word = embedding_model.wv.most_similar(key_word, topn=10)
print(sim_word)

# TSNE(t-Stochastic Neighbor Embedding)
vectors = []
labels = []
for label, _ in sim_word:
    # key_word와 유사한 단어들만 labels에 추가한다.
    labels.append(label)
    vectors.append(embedding_model.wv[label])

print(vectors[0])
print(len(vectors[0]))

# 데이터프레임 생성
df_vectors = pd.DataFrame(vectors)
print(df_vectors.head())

# 차원 축소
tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=2)
new_value = tsne_model.fit_transform(df_vectors)
df_xy = pd.DataFrame({'words': labels, 'x': new_value[:, 0], 'y': new_value[:, 1]})
print(df_xy.head())

# 산점도 그리기
