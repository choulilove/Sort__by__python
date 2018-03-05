class Queue(object):
    # 队列的实现，用线性表就是列表
    def __init__(self):
        self.__list = []

    # 入队
    def enqueue(self,item):
        self.__list.append(item)
        #self.__list.insert(0, item)

    # 出队
    def dequeue(self):
        return self.__list.pop(0)
        #return self.__list.pop()


    # 判断队列是否为空
    def is_empty(self):
        return self.__list == []



    # 返回队列的大小
    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    q =Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
