## 함수
def isQueueFull() :
    global SIZE, Queue, front, rear
    if (rear >= SIZE -1) :
        return True
    else : 
        return False

def isQueueEmpty() :
    global SIZE, Queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue():
    global SIZE, Queue, front, rear
    if(isQueueEmpty()) : 
        print('큐 텅!')
        return None
    front += 1
    data = queue[front]
    queue[front] = None

def enQueue(data) :
    global SIZE, Queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

 

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear= -1, -1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('유나')
# enQueue('꼬북이')
print('출구<---', queue, '<---입구')
retData = deQueue(); print('다음 손님 : ', retData)
retData = deQueue(); print('다음 손님 : ', retData)
# retData = deQueue(); print('다음 손님 : ', retData)
# print('출구<---', queue, '<---입구')
# retData = deQueue(); print('다음 손님 : ', retData)

enQueue('재남')