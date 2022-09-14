
import pickle

import matplotlib.pyplot as plt

img = plt.imread("블랙홀 배경.jpg") # 이미지파일 불러와서
with open('sample.pkl', 'wb') as f:
    pickle.dump(img, f) # pkl 파일로 저장

with open("sample.pkl", 'rb') as f:
    data = pickle.load(f)
    plt.imshow(data)
