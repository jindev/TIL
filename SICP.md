# 컴퓨터 프로그램의 구조와 해석
## 1. 프로시저를 써서 요약하는 방법
- 계산 프로세스
- 데이터
- 프로그램
- 식
- 프로그래밍 언어
- 제대로 프로그램 짜기

### Lisp 로 프로그램을 짠다는 것
- 프로시저와 데이터의 구분


### 1.1 프로그램 짤 때 바탕이 되는 것
- 프로그래밍 언어
  - 단순한 생각을 모아 복잡한 생각을 엮어내는 수단
  - expression
  - combination
  - abstraction

프로그래밍 언어를 사용해서 데이터와 프로시저를 나타내고, 프로시저들과 데이터들을 엮어서 복잡한것을 만들고, 이를 간단하게 요약하는 수단이 있어야 한다.

### 1.1.1 식
- combination
- operator
- operand
- argument

### 1.1.2 이름과 환경
- computaional object
- variable
- value
- environment
  - global

### 1.1.3 엮은식을 계산하는 방법
- combination
- subexpression
- recursive
- tree accumulation
- built-in operator

### 1.1.4 compound procedure
- procedure definition
- local name
- name
- formal parameters
- body

### 1.1.5 substitution model 으로 procedure를 실행하는 방법
```scheme
(define (square x) (* x x))

(define (sum-of-squares x y)
  (+ (square x) (square y)))

(define (f a)
  (sum-of-squares (+ a 1) (* a 2))
)

(f 5)
```

#### applicative order과 normal order
