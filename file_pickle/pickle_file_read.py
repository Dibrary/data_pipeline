
import pickle

with open("test1.p", "rb") as f: # 피클 파일 데이터는 binary이므로, rb꼴로 읽어야 한다.
    data = pickle.load(f)
    print(data)

# with open("test2.p", "rb") as f: # wb로 저장하지 않은 파일을 열려고 하면 EOFError: Ran out of input 에러 남.
#     print(pickle.load(f))

print("피클 데이터 읽기 끝.")

