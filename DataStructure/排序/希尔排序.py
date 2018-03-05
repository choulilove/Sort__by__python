"""希尔排序"""
def shell(alist):
    n = len(alist)
    gap = n//2
    while gap >= 1:

        # 插入排序
        for i in range(gap, n):
            j = i
            while j > 0:
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                j -= gap


        gap //= 2
    print(alist)

if __name__ == "__main__":
    li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    shell(li)

