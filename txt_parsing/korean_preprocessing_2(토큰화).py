
from konlpy.tag import Okt
tokenizer = Okt()
print(tokenizer.morphs("에이비식스 이대휘 1월 최애돌 기부 요정"))

print(tokenizer.pos("아버지가방에들어가신다"))

words = dict()
for x in tokenizer.pos("트랜잭션 애플리케이션은 테이블 스키마 변경이나 데이터베이스 시스템을 확장할 때 조심스럽게 계획을 세우고 많은 노력을 쏟아야 한다."):
    if x[0] not in words and x[1] == "Noun":
        words[x[0]] = 1

print(words) # 이렇게 하면 단어(특히 의미를 가진 단어)의 갯수를 저장할 수 있다.


from konlpy.utils import pprint
from konlpy.tag import Kkma

kkma = Kkma()
print(kkma.sentences(u'도움되셨다면, 공감을 눌러주세요.'))
