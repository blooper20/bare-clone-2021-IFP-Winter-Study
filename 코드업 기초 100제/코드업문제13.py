# 실수(float) 1개를 입력받아 저장한 후, 저장되어 있는 값을 소수점 셋 째 자리에서 반올림하여 소수점 이하 둘 째 자리까지 출력하시오.
# 내 풀이)
fl = float(input())
print(round(fl, 2))
# 강의 풀이)
var = round(float(input()), 2)
print(var)