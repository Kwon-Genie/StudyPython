'''
n개로 이루어진 정수 집합에서 원하는 수 k이상인 수가 처음으로 등장하는 위치를 찾으시오
단, 입력되는 집합은 오름차순으로 정렬되어 있으며, 같은 수가 여러개 존재할 수 있다.

'''

_list = [1, 3, 5, 7, 7]
find_num = 7

for i in range(len(_list)):
    if _list[i] >= find_num:
        print(i+1)
        break