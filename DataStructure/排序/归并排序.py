"""归并排序"""

def Merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left_list = Merge_sort(alist[:mid])
    right_list = Merge_sort(alist[mid:])
    left_point, right_point = 0, 0
    result = []
    while left_point < len(left_list) and right_point < len(right_list):
        if left_list[left_point] < right_list[right_point]:
            result.append(left_list[left_point])
            left_point += 1
        else:
            result.append(right_list[right_point])
            right_point += 1
    result += left_list[left_point:]
    result += right_list[right_point:]
    return result

if __name__ == "__main__":
    li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(li)
    list1 = Merge_sort(li)
    print(list1)



