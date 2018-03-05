"""选择排序"""
def selectSort(alist):
    n = len(alist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        if i != min_index:
            alist[i], alist[min_index] = alist[min_index], alist[i]




if __name__ == "__main__":
    list1 = [9, 0, 8, 4, 7, 5, 2, 1, 3]
    selectSort(list1)
    print(list1)






