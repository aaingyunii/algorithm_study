# 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 없다.

# 출력
# 서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.

# 예제 입력 

# 예제 출력 
# 2015-01-24

import datetime

print(datetime.datetime.now().strftime('%Y-%m-%d'))

## datetime 모듈을 import하고 now()메서드와 %Y, %m, %d 파싱하여 정답을 얻을 수 있었습니다.