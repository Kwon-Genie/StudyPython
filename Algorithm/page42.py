'''
창의적 알고리즘(중급) 42p 문제1
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 값이  몇 번째 수인지를 구하는 프로그램을 작성하라
예)
    3, 29, 38, 12, 57, 74, 40, 85, 61
    => 최댓값: 85, 8번째 수
'''

# 수 입력 받기
nums = list()
for i in range(9):
    nums.append(int(input()))

# 최댓값 찾기
max_num = 0
max_pos = 0
for i in range(len(nums)):
    if max_num < nums[i]:
        max_num = nums[i]
        max_pos = i + 1

print(max_num)
print(max_pos)


# python function 이용해서 더 편하게 구하기
print(max(nums))
print(nums.index(max(nums))+1) #0부터 시작이니까 +1 해줌 어차피 max로 찾고 index찾는거니까 없을리는 없즤