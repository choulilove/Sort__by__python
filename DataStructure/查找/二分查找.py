"""二分查找"""
def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    while first <= last:
        """
        X // Y 类型： 
　　　Floor除法：在Python 2.2中新增的操作，在Python2.6和Python3.0中均能使用，
     这个操作不考虑操作对象的类型，总是省略小数部分，剩下最小的能整除的整数部分。 
        """
        mid = (first + last)//2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False

if __name__ =="__main__":
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sign1 = binary_search(li, 5)
    sign2 = binary_search(li, 10)
    print(sign1)
    print(sign2)
