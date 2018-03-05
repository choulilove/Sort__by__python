"""递归二分查找"""
def binary_select(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
           return binary_select(alist[:mid-1], item)
        else:
           return binary_select(alist[mid+1:], item)

if __name__ =="__main__":
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sign1 = binary_select(li, 5)
    sign2 = binary_select(li, 10)
    print(sign1)
    print(sign2)