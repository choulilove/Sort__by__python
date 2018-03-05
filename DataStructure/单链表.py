# 单链表的实现

# 定义一个节点
class Node(object):
    def __init__(self, element):
        self.element = element
        self.next = None


# 定义一个单链表  共8个方法
class SingleLinkList(object):
    # 定义一个头指针
    def __init__(self):
        self._head = None
    # 头部添加元素
    def add(self,item):
        node = Node(item)
        node.next = self._head
        self._head = node



    # 尾部添加元素
    def append(self, item):
        pass



    # 插入元素
    def insert(self, pos ,item):
        pass
    # 移除元素
    def remove(self,item):
       pass
     # 查找元素
    def search(self,item):
        pass

    # 查看顺序表是否为空
    def is_empty(self):
      pass
    # 链表的长度
    def length(self):
       pass

    # 链表的遍历
    def travel(self):
       pass


if __name__ == "__main__":
    s = SingleLinkList()
    print(s.is_empty())
    s.append(10)
    s.append(20)
    s.append(40)
    s.append(50)
    s.append(60)
    s.append(70)
    s.append(80)
    s.append(90)
    print(s.is_empty())
    s.add(30)
    s.travel()
    s.remove(30)
    s.travel()
    s.remove(90)
    s.travel()
    s.remove(60)
    s.travel()