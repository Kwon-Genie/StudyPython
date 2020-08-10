#python 정리
# # 표준 입력
# a = input()
# # 표준 출력
# print(a)

# # 표준 출력 서식
# print('%s' %('Hello World')) #문자열 string
# print('%c'%'H') #문자 character
# print('%d'%100) #정수
# print('%o'%10) #8진수
# print('%x'%10) #16진수
# print('%f'%10.6) #실수 float
#
# # 표준 출력 서식 str.format()
# # 문자열.format(서식)
# print('{} {}'.format('Hello','World')) #문자열 string
# print('{}'.format('H')) #문자 character
# print('{0:d}'.format(100)) #정수
# print('{0:o}'.format(10)) #8진수
# print('{0:x}'.format(10)) #16진수
# print('{0:f}'.format(10.6)) #실수 float

# # type 확인
# a = 'test'
# b = 10
# c = 10.5
# d = '%x'%10
# e = bin(10)
# f = oct(8)
# g = hex(16)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d), d) # 16진수는 str 타입으로 분류되네
# print(type(e),e) #2진수이기 떄문에 앞에 0b가 붙는다 그래도 str
# print(type(f),f) #8진수이기 때문에 앞에 0o가 붙는다 그래도 str
# print(type(g),g) #16진수이기 때문에 앞에 0x가 붙는다 그래도 str
#
# # bit = 0/1
# # byte => 8개의 bit가 모인 것
# # 2byte => 1character print('{0:x}'.format(10))

# #연산자
# print(1+1) #더하기
# print(1-1) #빼기
# print(2*3) #곱하기
# print(4/3) #나누기 => 자동으로 실수로 변환된다 casting 필요없음
# print(4//3) #나누기의 몫 구하기
# print(6%4) #나누기의 나머지 구하기
# print(5**3) #제곱 구하기
#
# # 논리 연산자
# # and, or, not
# if not False :
#     print(True)

# # 조건문
# a = 'tt'
# if a == 't' :
#     print('a is t')
# elif a=='ttt' :
#     print('a is {}'.format(a))
# else :
#     print('a is %s'%(a))

# # 반복문 for/while
# # for 변수 in 시퀀스형객체
# # for 변수 in range(start,stop,step) range의 start부터 stop-1까지 step만큼 증가하여 변수 i return
# for i in 'hello' :
#     print(i, end=' ')
# print()
# for i in ['a','b'] :
#     print(i, end=' ')
# print()
# for i in {'a':'b','c':'d'} :
#     print(i, end=' ')
# print()
# for i in range(10) :
#     print(i, end=' ')
# print()
# for i in range(1,10) :
#     print(i, end=' ')
# print()
# for i in range(1, 10, 2) :
#     print(i, end=' ')
# print()

# # 예)구구단
# for i in range(1, 10) :
#     for j in range(2, 10) :
#         print('{:<2}X{:>2} = {:>2}'.format(j,i,i*j), end='   ')
#     print()

# # continue
# for i in range(1, 11) : #=> 3을 빼고 출력한다는걸 알 수 있음
#     if i == 3 :
#         continue
#     print(i, end=' ')
#
# # break
# print()
# for i in range(1, 11) : # 3에서 break를 만나서 for문이 중단되는것을 알 수 있음
#     if i == 3 :
#         break
#     print(i, end=' ')

# print("what's your name?")

# # 문자열 slicing
# a = '123456789'
# print(a[0])
# print(a[0:1])
# print(a[2:6])
# print(a[5:])
# print(a[:4])
# print(a[-1])
# # 문자열 더하기
# a = '123'
# b = a
# b += '345'
# print(a)
# print(b)
# # 문자열 곱하기
# a = '1'*5
# print(a)

# # 문자열 관련 함수
a = 'Hello World!'
# print(a.upper()) #대문자 변환
# print(a.lower()) #소문자 변환
# print(a.swapcase()) #대문자 <-> 소문자 변환
# print(a.lower().title()) #단어의 첫 문자 대문자 변환
# print(a.lower().capitalize()) #첫문자 대문자 변환
# print(a.count('o')) #특정 문자 몇 번 반복되었는지 반환
# print(a.find('x'), a.find('o')) #해당 문자열의 위치를 반환함 없는 문자열은 -1을 반환
# print(a.find('o'), a.find('o',6), a.find('o',10)) #해당 문자열의 index부터 찾고자하는 문자열이 위치하는 곳 검색하여 인덱스 반환
# print(a.rfind('o')) # 해당 문자열의 끝부터 시작하여 특정 문자열이 검색되는 인덱스 반환, 존재하지 않으면 -1 반환
# print(a.index('o'), a.index('test')) #문자열에서 찾는 첫번째 위치 반환 없을 경우는 error 발생 => ValueError
# print(a.rindex('o')) #, a.rindex('test'))  #문자열의 긑부터 시작해서 문자열을 찾아 첫번째 위치를 반환, 없을 경우는 error 발생
# print(a.startswith('d'), a.startswith('h'), a.startswith('H')) #해당문자열이 특정문자열로 시작하는지 판단
# print(a.endswith('d'), a.endswith('!'), a.endswith('H')) #해당문자열이 특정문자열로 끝나는지 판단
# print(' difjlkjsdflkj lkfjlskdjf    '.strip()) #문자열의 좌우 공백 제거
# print(a.strip('H')) #문자열의 좌우에 있는 특정 문자 제거
# print('  dsfsdf sdfsdf    '.rstrip()) #문자열의 오른쪽 공백을 제거함함
# print('  123 123123132    '.lstrip(),'t') #문자열의 왼쪽 공백을 제거
# print(a.replace('o','O')) #문자열의 특정 문자열을 대체문자로 변경  var.replace('특정문자','대체문자')
# print(a.split(), a.split('o')) #문자열 분할 함
# print('ff dfdf dfdf '.split(), 'ff dfdf dfdf '.rsplit()) #문자열 오른쪽부터 공백을 기준으로 분리해서 리스트 만들어
# print('lkjlkjflj\ndfdfdf \nㅇㄹㅇㄹㅇㄹ ㅇㄹㅇ'.splitlines()) #라인 단위로 분리하여 리스트를 만들어줌
# print('+'.join('this sentence')) #문자열을 포함할 문자와 함께 결합
# print(a.center(20,'0')) #문자 중앙 정렬 var.center(자리수,채울문자) => 채울문자에 숫자 넣으면 TypeError 뱉어냄
# print(a.ljust(20, '0')) #문자열 왼쪽 정렬
# print(a.rjust(20,'0')) #문자열 오른쪽 정렬
# print(a.zfill(20)) #문자열 오른쪽 정렬 & 0으로 빈자리 채움
# print(a.isdigit(), '123'.isdigit()) #문자열이 숫자로 구성되었는지 확인
# print(a.isalpha(), '123'.isalpha(), '확인'.isalpha(), 'HelloWorld'.isalpha()) #문자열이 영문자로 구성되었는지 확인 => 문자열에 공백, 숫자, 특수기호 등 이 포함되어있으면 False 반환
# print(a.isalnum(), '123'.isalnum(), 'abc'.isalnum(), '123abc'.isalnum()) #문자, 숫자로만 구성되어있으면 True / 공백과 같은 특수문자 포함시 False 반환
# print(a.islower(), '123'.islower(), 'abc'.islower(), 'ABC'.islower(), '하하'.islower()) #영문자 소문자로만 구성되어있는 문자열의 경우 True 이외는 False
# print(a.isupper(), '123'.isupper(), 'abc'.isupper(), 'ABC'.isupper(), '하하'.isupper()) #영문자 대문자로만 구성되어있는 문자열의 경우 True 이외는 False
# print(a.isspace(), '  '.isspace(), '123'.isspace(), 'abc'.isspace(), '하하'.isspace(), '$$'.isspace()) #공백문자로만 구성되어있는 문자열의 경우 True 이외는 False
# print(a.istitle(), '123'.istitle(), 'Hello world!'.istitle()) #문자열의 첫문자가 대문자인지 확인 Hello World와 같은 구성의 경우 True
# print(str(123), int(123), ord('a')) # str(): string convert / int(): int convert / ord(): ascii unicode convert
# print(list(a)) #string -> list로 쪼개는 함수

# # error 처리
# try :
#     print(a.index('o'), a.index('test')) #문자열에서 찾는 첫번째 위치 반환 없을 경우는 error 발생 =>
# except ValueError :
#     print('error')

