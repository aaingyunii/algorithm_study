# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

# 예제 입력 
# 5
# 20 10 35 30 7

# 예제 출력 
# 7 35

# 처음에 짠 코드
# n = int(input("Num of numbers : "))

# nums = list(map(int,input().split()))

# print(nums)
# print("Max num :",max(nums))
# print("Min num :",min(nums))


# 백준 제출 정답
n = input()
nums = list(map(int,input().split()))
print(min(nums),max(nums))


## 처음에 짠 코드로 제출했을 떄 출력 초과로 오류가 났었고, 예제 출력의 순서로 바꾸고 nums 출력을 빼고 제출했을 때도 틀렸습니다.
## 알고보니 문제에서 메모리 제한과 시간 제한을 생각치 못하고 보기 좋게 하려고 출력문에 문자열도 추가하다보니 문제의 제한에 걸려
## 이러한 결과가 나타났습니다. 이후 아래 코드처럼 간략하게 변환 후 정답을 얻을 수 있었습니다.