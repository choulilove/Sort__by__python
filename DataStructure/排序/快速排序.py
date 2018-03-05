"""快速排序"""
def quick_sort(alist, first, last):
    if first > last:
        return
    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] > mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)

if __name__ == "__main__":
    list1 = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    quick_sort(list1, 0, len(list1)-1)
    print(list1)