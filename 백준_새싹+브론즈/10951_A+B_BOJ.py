# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.

# 예제 입력  
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2
# 예제 출력 
# 2
# 5
# 7
# 17
# 7

## 종료 조건이 없음.
## 명확한 종료 조건이 없기 때문에 입력이 없으면 테스트 케이스가 끝난다.
while 1 :
    try:
        a,b= map(int,input().split())
        print(a+b)

    except:
        break

## 처음에 억지로 종료조건을 만들어서 제출했으나, 이는 틀렸고,
## 그러면 무한 입력상태에서 입력이 없으면 반복문이 끝나는 것으로 고쳐 제출하여 정답을 얻음!