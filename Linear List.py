## 함수
def add_data(friend) :
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 친구 입력
    katok[kLen-1] = friend

def insert_data(position, friend) :
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 한칸씩 옆으로 이동
    for i in range(kLen-1, position, -1) : # 중요! 어려움.
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계 : 친구 입력
    katok[position] = friend

def delete_data(position):
    # 1단계 : 데이터 삭제
    katok[position] = None
    kLen = len(katok)
    # 2단계 : 한칸씩 앞으로 이동
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    # 3단계
    del(katok[kLen-1])

## 전역
katok = []
select = -1

## 메인
if __name__ == '__main__':

    while(select != 4):

        select = int(input("선택하세요(1: 추가, 2:삽입, 3:삭제, 4:종료)--> "))

        if(select == 1):
            data = input('추가할 데이터 --> ')
            add_data(data)
            print(katok)
        elif(select == 2):
            pos = int(input('삽입할 위치 --> '))
            data = input('추가할 데이터 --> ')
            insert_data(pos, data)
            print(katok)
        elif(select == 3):
            pos = int(input('삭제할 위치 --> '))
            delete_data(pos)
            print(katok)
        elif(select == 4):
            print(katok)
            exit
        else:
            print('1~4 중 하나를 입력하세요.')
            continue