from celery import Celery
app = Celery('tasks', backend='rpc://', broker='pyamqp://guest:guest@localhost//')

@app.task
def add(x, y):
    return x + y


'''
정상 실행 완료.
countdown으로 실행 순간을 미룰 수도 있다.

signature를 사용해서 다른 함수나 프로세스로 전달도 가능하다.
'''