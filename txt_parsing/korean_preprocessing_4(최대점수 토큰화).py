
from soynlp.tokenizer import LTokenizer
from soynlp.word import WordExtractor
from soynlp import DoublespaceLineCorpus

corpus = DoublespaceLineCorpus('apache_flink.txt')
print(len(corpus)) # 562줄 있다고 나옴.

i = 0
for doc in corpus:
    print(doc)
    i += 1
    if i == 10:
        print(" ")
        break


word_extractor = WordExtractor()
word_extractor.train(corpus)
word_score_table = word_extractor.extract()

scores = {word:score.cohesion_forward for word, score in word_score_table.items()}
l_tokenizer = LTokenizer(scores = scores)

print(l_tokenizer.tokenize("국제사회와 우리의 노력으로 범죄를 척결하자", flatten=False))
# 이거도 못써먹겠음. 제대로 못 자름.

from soynlp.tokenizer import MaxScoreTokenizer

maxscore_tokenizer = MaxScoreTokenizer(scores = scores)
print(maxscore_tokenizer.tokenize("국제사회와우리의노력으로범죄를척결하자"))
# 이건 못써먹겠다. 제대로 못 자름.

