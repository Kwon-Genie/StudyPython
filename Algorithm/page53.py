'''
n 개로 이루어진 정수 집합에서 원하는 수의 위치를 찾으시오
단, 입력되는 집합은 오름차순으로 정렬되어있으며, 같은 수는 없다.

입력: 첫 줄에 한 정수 n이 입력됨
     둘쨰 줄에 n개의 정수가 공백을 구분되어 입력됨
     셋쨰 줄에는 찾고자 하는 수가 입력됨. 단, 2 <= n <= 1000000  각 원소의 크기는 100000000을 넘지 않는다
'''
#편의상 그냥 이렇게 써봄..
num_cnt = 8
num_list = [1, 2, 3, 5, 7, 9, 11, 15]
find_num = 30
result_pos = -1

for i in range(len(num_list)):
    if num_list[i] == find_num:
        result_pos = i+1
        break

print(result_pos)

#python이니까 다르게도 해볼까
try :
    result_pos = num_list.index(find_num)
except ValueError:
    pass #얘가 오류를 그냥 skip할 수 있게 해주는 애임 list.index(val) 에서 value가 없는 수이면 ValueError를 반환하니까 pass 시키려고..!
    # result_pos = -1
#     그냥 끝낼수는 없나 컨티뉴하면 되나?

print(result_pos)
