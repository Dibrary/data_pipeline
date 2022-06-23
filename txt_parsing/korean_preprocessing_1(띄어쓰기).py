
'''
스페이스를 넣어주는 기능인 pykospacing모듈

설치하려면
pip install git+https:/github.com/haven-jeon/PyKoSpacing.git
입력해야 한다.

대용량 코퍼스를 학습해 만들어진 띄어쓰기 딥러닝 모델.

관련 패키지는
Installing collected packages: tensorflow-estimator, keras, cached-property, argparse, urllib3, h5py, tensorflow, pykospacing

'''

new_sent = "김철수는극중두인격의사나이이광수역을맡았다.철수는한국유일의태권도전승자를가리는결전의날을앞두고10년간함께훈련한사형인유연재(김광수분)을찾으러속세로내려온인물이다."


from pykospacing import spacing
kospacing_sent = spacing(new_sent)
print(kospacing_sent)


