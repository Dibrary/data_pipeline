
from txt_parsing.txtFile_reading import title, contents

word_counts = dict()

for sentence in contents:
    if sentence == "\n": # 단순히 \n만 있는 경우 제거
        continue
    else:
        for word in sentence.split():
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

print(word_counts)
print(len(word_counts)) # 전체 단어 갯수가 2112 , 조사나 접미사 등등 단어가 아닌 것을 떼면 중복되는게 많이 있을 것;
print(word_counts["="]) # 그냥 = 만 있는 것도 69개나 있다.





