
from soynlp.normalizer import *

print(emoticon_normalize('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ이 영화 ㅋㅋㅋㅋㅋ ㅋㅋㅋㅋㅋㅋㅋㅋ'))

print(emoticon_normalize('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ이 영화 ㅋㅋㅋㅋㅋ ㅋㅋㅋㅋㅋㅋㅋㅋ', num_repeats=2)) # 반복되는 부분은 2개만 남김.

