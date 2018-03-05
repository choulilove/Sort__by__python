def insertSort(alist):
    n = len(alist)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
    print(alist)
if __name__ == "__main__":
    list1 = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    insertSort(list1)
