'''双端队列'''
class Queue:
    def __init__(self):
        self.__list = []

    # 在队列中添加一个元素‘
    def add_front(self,item):
        self.__list.insert(0,item)
    # 在队列中添加一个元素
    def add_rear(self,item):
        self.__list.append(item)
    # 在队列中取出一个元素
    def pop_front(self):
        self.__list.pop(0)
    def pop_rear(self):
        self.__list.pop()
    # 判断队列是否为空
    def is_empty(self):
       return self.__list == []
    # 判断队列中元素的个数
    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    q = Queue()


