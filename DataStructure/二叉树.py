"""二叉树"""
"""
#return使用说明:  
#(1)返回函数的返回值  
#(2)终止程序的运行，提前退出.(例如:当函数内有错误发生时，使用return可以终止函数的运行) 
"""

# 定义一个结点
class Node(object):
    def __init__(self, item=-1, lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

# 定义一个树
class Tree(object):
    def __init__(self):
        self.root = None
    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = []
        queue.append(self.root)
        while queue:
            cur = queue.pop(0)
            if cur.lchild is None:
                cur.lchild = node
                return
            else:
                queue.append(cur.lchild)
            if cur.rchild is None:
                cur.rchild = node
                return
            else:
                queue.append(cur.rchild)
    def breath_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
    def preorder(self, node):
        if node is None:
            return
        print(node.item, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.item, end=" ")
        self.inorder(node.rchild)
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.item, end=" ")
if __name__ == "__main__":
   tree = Tree()
   tree.add(1)
   tree.add(2)
   tree.add(3)
   tree.add(4)
   tree.add(5)
   tree.add(6)
   tree.add(7)
   tree.add(8)
   tree.add(9)
   print("深度遍历")
   tree.breath_travel()
   print(" ")
   print("前序遍历")
   tree.preorder(tree.root)
   print(" ")
   print("中序遍历")
   tree.inorder(tree.root)
   print(" ")
   print("后序遍历")
   tree.postorder(tree.root)









