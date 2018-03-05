def insert_sort(alist):
    n = len(alist)

    for i in range(1, n):
        """ { 9 ,[1, 8, 2, 7, 3, 6, 4, 5]}
        从[1, 8, 2, 7, 3, 6, 4, 5]取出元素进行排序
        """
        # i负责不断的拿去数据
        j = i
        while j > 0:
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
            j -= 1
    print(alist)

if __name__ == "__main__":
    li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    insert_sort(li)