# Generator
# Iteration 동작 제어
# 메모리 어딘가에 저장해놓을 필요가 없음.
# yield 구문 사용 -> 중간값 리턴, 함수는 맨 끝에 도달할 때 까지 실행.
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


# 함수의 리턴값은 제너레이터.
get_natural_number()
# <generator object get_natural_number at 0x10d3139d0 >


# 다음 값을 생성하려면 next()


# 여러 타입의 값을 하나의 함수에서 생성하는 것도 가능
def generator():
    yield 1
    yield 'string'
    yield True
# >>> g = generator()
# >>> g
# <generator object generator at 0x10z47c678>
# >>> next(g)
# 1
# >>> next(g)
# 'string'
# >>> next(g)
# True
