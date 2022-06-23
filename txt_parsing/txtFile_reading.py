
# with open("apache_flink.txt", "r") as f:
#     print(f)

# 그냥 위 코드 실행하면
# 이런 결과 나옴 <_io.TextIOWrapper name='apache_flink.txt' mode='r' encoding='cp949'>

contents = []
title = ""

with open("apache_flink.txt", "r", encoding="UTF8") as f:
    # print(f.read()) # 이렇게 하면 해당 줄 모조리 읽어온다.

    for idx, k in enumerate(f.readlines()): # 항상 첫 번째 줄에 제목이 온다고 가정할 때 
        if idx == 0:
            title = k # 제목 뽑아내기
        else:
            contents.append(k)





