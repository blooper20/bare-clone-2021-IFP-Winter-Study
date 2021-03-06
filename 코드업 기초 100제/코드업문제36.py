# 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
# 내 풀이)
one, two = map(int, input().split())
hap = one + two
print(hap)
# 강의 풀이)
a, b = map(int, input().split())
print( a+b )
# 실제 문제에서는 굉장히 넓은 정수 범위의 데이터형을 요구하는 문제이나 파이썬에서는 int()로 처리가 가능하다.
# 예를 들어 C에서 unsinged int보다도 크며 unsinged long과 같은 범위를 지니고 있다고 한다.
# 실제 범위
# 범위 : -9223372036854775808 ~ 9223372036854775807
# 이보다 큰 범위를 지정하고자 할 때는 long 데이터 형을 이용하면 된다.
# 파이썬에서는 4가지의 데이터형을 제공한다.