import pickle

data = {}
data[1] = {'no': 2, 'subject': '안녕 피클', 'content': '피클은 매우 간단합니다.'}

with open('test1.p', 'wb') as f: # binary로 저장이 된다.
    pickle.dump(data, f)

# with open('test2.p', 'w') as f: # pickle로 파일 생성하려고 할 때 b를 빼먹으면 안 된다.
    # TypeError: write() argument must be str, not bytes 에러
    # pickle.dump(data, f)

print("피클 파일 생성 완료.")
