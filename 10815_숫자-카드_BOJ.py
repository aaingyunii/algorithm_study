import time

s= time.time() # 시작 시간

n = int(input()) # 상근이가 가지고 있는 숫자 카드의 개수
nums_list = list(map(int, input().split())) #  숫자 카드에 적혀있는 정수
                                        # -10,000,000<=nums <10,000,000
m = int(input()) # M
correct = list(map(int, input().split())) # 숫자 카드인지 아닌지를 구해야 할 M개의 정수
correct_list = [] # 숫자 카드 인지 아닌지 확인한 결과 저장 리스트

for x in correct:
    if x in nums_list:
        correct_list.append(1)
    else:
        correct_list.append(0)

print(correct_list)

e= time.time()
print(f"{e - s:.5f} sec")

### 위 제출결과 : 시간 초과.

## 탐색 과정에 대해 학습하고 다시 풀어보자!



