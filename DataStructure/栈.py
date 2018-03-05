# 定义一个类
# 用顺序表实现栈，与链表实现是不同的
class Stack(object):
    def __init__(self):
        self.__list= []
    # 进栈
    def push(self,item):
        self.__list.append(item)
    # 出栈
    def pop(self):
        print(self.__list.pop())
    # 返回栈顶元素
    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None
    # 返回元素个数
    def size(self):
        return len(self.__list)
    # 判断栈中元素是否为空
    def is_empty(self):
        return self.__list == []

if __name__== "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    print(s.is_empty())
    print(s.peek())
    print(s.size())

