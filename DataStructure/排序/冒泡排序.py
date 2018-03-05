"""冒泡排序"""
def bubbleSort(lst):
    # 需要排序的序列的长度
    n = len(lst)
    for i in range(n-1):
        count = 0
        # 每次排序出来一个最大值
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                count += 1
        if 0 == count:
            return
    print(lst)

if __name__ == "__main__":
    lst = [3, 4, 1, 2, 5, 8, 0]
    bubbleSort(lst)
