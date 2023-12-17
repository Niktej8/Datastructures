#!/usr/bin/env python
# coding: utf-8

# # Data Structures

# In[102]:


pip install nb_black


# In[112]:


get_ipython().run_line_magic('load_ext', 'nb_black')


# ### Stack using list

# In[104]:


class Stack:
    def __init__(self):
        self.l = []

    def size(self):
        return len(self.l)

    def traversal(self):
        if len(self.l) == 0:
            return "Queueu is Empty"
        return self.l

    def push(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop()

    def peek(self):
        if self.size() == 0:
            return "Stack is empty"
        return self.l[-1]


s = Stack()
s.push(10)
s.push(18)
s.push(12)
s.pop()
print(s.peek())
s.traversal()


# ### Stack using deque module

# In[14]:


import collections
stack = collections.deque()
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack[-1])
print(stack)


# ### Stack using LifoQueue Module

# In[15]:


import queue
stack = queue.LifoQueue(4)
stack.put(10)
stack.put(20)
stack.put(30)
stack.get()
stack.put(40)
stack.put(50,timeout =1)
stack.get()


# ### Queue using List

# In[16]:


class Queue:
    def __init__(self):
        self.lis=[]
    def traversal(self):
        if len(self.lis)==0:
            return "Queueu is Empty"
        return self.lis
    def size(self):
        return len(self.lis)
    def enqueue(self,x):
        self.lis.append(x)
    def dequeue(self):
        if self.size() == 0:
            return "Queue is Empty"
        return self.lis.pop(0)
    def top(self):
        return self.lis[-1]  
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.dequeue()
q.enqueue(30)
q.dequeue()
q.enqueue(50)
print(q.top())
q.traversal()


# ### Queue using Deque

# In[17]:


# We can use either of these appendleft,pop or append,popleft
import collections
queue = collections.deque()
queue.appendleft(10)
queue.appendleft(20)
queue.appendleft(30)
queue.pop()
queue.pop()
queue


# ### Implementing Queue using Stack
# 
# ####  Implementing Queue by using 2 stacks
# ####  Implementing Queue by using Input and Output Stack

# In[21]:


import copy
class Queue:
    def __init__(self):
        self.lis=[]
    def traversal(self):
        if len(self.lis)==0:
            return "Queueu is Empty"
        return self.lis
    def size(self):
        return len(self.lis)
    def enqueue(self,x):
        self.lis.append(x)
    def dequeue(self):
        if self.size() == 0:
            return "Queue is Empty"
        return self.lis.pop(0)
    def top(self):
        return self.lis[-1]  

# Implementing Queue by using 2 stacks
class Queue_using_2stacks(Stack):
    def __init__(self):
        super().__init__()
        self.s1 = Stack()
        self.s2 = Stack()
    def enqueue(self,x):
        for i in range(self.s1.size()):
            self.s2.push(self.s1.pop())
        self.s1.push(x)
        for i in range(self.s2.size()):
            self.s1.push(self.s2.pop())
    def dequeue(self):
        return self.s1.pop()
    def top(self):
        return self.s1.peek()
    def traversal(self):
        return self.s1.traversal()

# c =  Queue_using_2stacks()
# c.enqueue(10)
# c.enqueue(20)
# c.enqueue(30)
# print(c.top())
# print(c.dequeue())
# c.traversal()

# Implementing Queue by using Input and Output Stack
class Queue_in_out_2stack(Stack):
    def __init__(self):
        super().__init__()
        self.input = Stack()
        self.output = Stack()
    def enqueue(self,x):
        self.input.push(x)
    def dequeue(self):
        if self.output.size()!=0:
            return self.output.pop()
        else:
            for i in range(self.input.size()):
                self.output.push(self.input.pop())
            return self.output.pop()
    def top(self):
        if self.output.size()!=0:
            return self.output.peek()
        else:
            for i in range(self.input.size()):
                self.output.push(self.input.pop())
            return self.output.peek()
    def traversal(self):
        if self.input.size() !=0:
            return "input - ",self.input.traversal()
        return "output - ",self.output.traversal()
# d = Queue_in_out_2stack()
# d.enqueue(4)
# d.enqueue(3)
# d.enqueue(2)
# print(d.top())
# print(d.dequeue())
# d.traversal()


# ### Implement Stack Using Queue
# #### Implement Stack Using Double Queues
# #### Implement Stack using Single Queue

# In[22]:


import copy
class Queue:
    def __init__(self):
        self.lis=[]
    def traversal(self):
        if len(self.lis)==0:
            return "Queueu is Empty"
        return self.lis
    def size(self):
        return len(self.lis)
    def enqueue(self,x):
        self.lis.append(x)
    def dequeue(self):
        if self.size() == 0:
            return "Queue is Empty"
        return self.lis.pop(0)
    def top(self):
        return self.lis[-1]  
# q=Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.dequeue()
# q.enqueue(30)
# q.dequeue()
# q.enqueue(50)
# print(q.top())
# q.traversal()

#Implement Stack Using Queues
class Stack_using_2Queues(Queue):
    def __init__(self):
        super().__init__()
        self.q1 = Queue()
        self.q2 = Queue() 
    def push(self,x):
        self.q2.enqueue(x)
        for i in range(self.q1.size()):
            self.q2.enqueue(self.q1.dequeue())
        self.q1=copy.deepcopy(self.q2)
        for i in range(self.q1.size()):
            self.q2.dequeue()
    def pop(self) :
        return self.q1.dequeue()
    def top(self):
        return self.q1.top()
    def traversal(self):
        return self.q1.traversal()
    
class Stack_using_1Queue(Queue):
    def __init__(self):
        super().__init__()
        self.q1 = Queue()
    def push(self,x):
        self.q1.enqueue(x)
        for i in range(self.q1.size()-1):
            self.q1.enqueue(self.q1.dequeue())
    def pop(self) :
        return self.q1.dequeue()
    def top(self):
        return self.q1.top()
    def traversal(self):
        return self.q1.traversal()

# x = Stack_using_2Queues()
# x.push(10)
# x.push(20)
# x.push(30)
# x.push(40)
# print("After pop - ",x.pop())
# print("Top -",x.top())
# x.traversal()

y = Stack_using_1Queue()
y.push(10)
y.push(20)
y.push(30)
y.push(40)
print(y.pop())
y.traversal()


# ### Single Linked List all operations

# In[162]:


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class Linked_List(Node):
    def __init__(self):
        self.head = None

    def add_first(self, data):
        if self.head == None:
            newnode = Node(data)
            self.head = newnode
        else:
            newnode = Node(data)
            newnode.ref = self.head
            self.head = newnode

    def add_last(self, data):
        if self.head == None:
            newnode = Node(data)
            self.head = newnode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            newnode = Node(data)
            n.ref = newnode

    def add_after(self, x, data):
        if self.head is None:
            raise Exception("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.ref
            else:
                raise Exception("Given Node value is not Present")
            newnode = Node(data)
            newnode.ref = n.ref
            n.ref = newnode

    def add_before(self, x, data):
        if self.head is None:
            raise Exception("Linked List is empty")
        else:
            if self.head.data == x:
                newnode = Node(data)
                newnode.ref = self.head
                self.head = newnode
            else:
                n = self.head
                while n.ref is not None:
                    if n.ref.data == x:
                        break
                    n = n.ref
                else:
                    raise Exception("Given Node value is not Present")
                newnode = Node(data)
                newnode.ref = n.ref
                n.ref = newnode

    def delete_first(self):
        if self.head is None:
            raise Exception("Since Linked List is empty, we cant delete any thing")
        else:
            self.head = self.head.ref

    def delete_last(self):
        if self.head is None:
            raise Exception("Since Linked List is empty, we cant delete any thing")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_element(self, x):
        if self.head is None:
            raise Exception("Since Linked List is empty, we cant delete any thing")
        elif self.head.data == x:
            self.head = self.head.ref
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            else:
                raise Exception("Given Node value is not Present")
            n.ref = n.ref.ref

    def traversal(self):
        n = self.head
        if n is None:
            return "Linked List is Empty"
        while n is not None:
            print(n.data, end="-->")
            n = n.ref

    def size(self):
        count = 0
        n = self.head
        if n is None:
            return count
        while n is not None:
            count += 1
            n = n.ref
        return count

    def search_element(self, x):
        n = self.head
        while n is not None:
            if n.data == x:
                return True
            n = n.ref
        else:
            return False

    def middle_element_naive(self):
        l = self.size()
        mid = (l // 2) + 1
        c = 0
        n = self.head
        while n is not None:
            c += 1
            if c == mid:
                break
            n = n.ref
        print(n.data)

    def middle_element_optimal(self):
        """
        Tortoise and Hare Algorithm where slow pointer will do 1 step
        and fast pointer will do 2 steps
        """
        if self.head is None:
            raise Exception("Linked List is empty")
        else:
            slow_pointer = self.head
            fast_pointer = self.head
            while fast_pointer and fast_pointer.ref is not None:
                slow_pointer = slow_pointer.ref
                fast_pointer = fast_pointer.ref.ref
            print(slow_pointer.data)

    def reverse(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        else:
            temp = self.head
            prev = None
            while temp is not None:
                nex = temp.ref
                temp.ref = prev
                prev = temp
                temp = nex
            self.head = prev

    def check_cyclic(self):
        if self.head is None:
            return False
        else:
            slow_pointer = self.head
            fast_pointer = self.head
            while fast_pointer and fast_pointer.ref is not None:
                slow_pointer = slow_pointer.ref
                fast_pointer = fast_pointer.ref.ref
                if slow_pointer == fast_pointer:
                    return True
            return False


# l = Linked_List()
# l.add_first(10)
# l.add_first(20)
# l.add_last(30)
# l.add_last(40)
# l.add_last(50)
# l.add_last(60)
# l.traversal()
# print()
# l.add_after(x=20,data=60)
# l.traversal()
# l.add_before(x=40,data=100)
# l.size()
# l.traversal()
# print()
# l.delete_first()
# l.delete_last()
# l.delete_element(10)
# print(l.search_element(10))
# l.traversal()
# print()
# l.middle_element_naive()
# l.middle_element_optimal()
# l.reverse()
# l.traversal()
# l.check_cyclic()


# ### Doubly Linked List All Operations

# In[78]:


class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None
        self.nref = None


class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            self.head.pref = newnode
            newnode.nref = self.head
            self.head = newnode

    def add_last(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = newnode
            newnode.pref = n

    def add_after(self, x, data):
        if self.head is None:
            raise Exception("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            else:
                raise Exception("Given Node value is not Present")
            newnode = Node(data)
            newnode.nref = n.nref
            newnode.pref = n
            if n.nref is not None:
                n.nref.pref = newnode
            n.nref = newnode
            
    def add_before(self,x,data):
        if self.head is None:
            raise Exception("Linked List is empty")
        elif self.head.data == x:
            newnode =Node(data)
            newnode.nref = self.head
            self.head.pref = newnode
            self.head=newnode
        else:
            n=self.head
            while n.nref is not None:
                if n.nref.data == x:
                    break
                n=n.nref
            else:
                raise Exception("Given Node value is not Present") 
            newnode = Node(data)
            newnode.pref = n
            newnode.nref = n.nref
            n.nref = newnode
            n.nref.pref = newnode

    def del_first(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        elif self.head.nref is None:
            self.head=None
        else:
            self.head = self.head.nref
            self.head.pref =None
    def del_last(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        elif self.head.nref is None:
            self.head=None
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref = None
    def del_by_value(self,x):
        if self.head is None:
            raise Exception("Linked List is empty")
        elif self.head.nref is None:
            if self.head.data == x:
                self.head = None
        elif self.head.data == x:
            self.head = self.head.nref
            self.head.pref =None
        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nref
            else:
                raise Exception("Given Node value is not Present") 
            if n.nref is not None:
                n.pref.nref = n.nref
                n.nref.pref = n.pref
            else:
                n.pref.nref = None
    def ftraversal(self):
        n = self.head
        if n is None:
            return "Doubly Linked List Is Empty"
        while n is not None:
            print(n.data, end="->")
            n = n.nref
            
    def reverse(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        else:
            curr = self.head
            while curr is not None:
                last = curr.pref
                curr.pref = curr.nref
                curr.nref = last
                curr = curr.pref
            if last:
                self.head = last.pref

dll = Doubly_Linked_List()
dll.add_first(10)
dll.add_first(20)
dll.add_first(30)
dll.add_first(40)
dll.add_last(50)
dll.add_after(50, 60)
# dll.add_before(20,8)
# dll.del_first()
dll.del_last()
# dll.del_by_value(40)
dll.ftraversal()
dll.reverse()
print()
dll.ftraversal()


# ### Circular Linked Lists All Operations

# In[85]:


class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Circular_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_begin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            newnode.ref=self.head
            self.tail=newnode
        if self.head is not None:
            newnode.ref=self.head
            self.head=newnode
            self.tail.ref=newnode
    def add_end(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.ref = self.head
            self.tail = newnode
        else:
            self.tail.ref = newnode
            newnode.ref = self.head
            self.tail = newnode
    
    def add_after(self,x,data):
        if self.head is None:
            raise Exception("Linked List is empty")
        elif self.tail.data ==x:
            newnode = Node(data)
            self.tail.ref = newnode
            newnode.ref = self.head
            self.tail = newnode
        else:
            n = self.head
            while n is not None:
                if n.data==x:
                    break
                n = n.ref
                if n==self.head:
                    break
            if n==self.head:
                raise Exception("Given Node value is not Present") 
            else:
                newnode = Node(data)
                newnode.ref = n.ref
                n.ref=newnode
    def add_before(self,x,data):
        if self.head is None:
            raise Exception("Linked List is empty")
        elif self.head.data == x:
            newnode = Node(data)
            newnode.ref = self.head
            self.head = newnode
            self.tail.ref = newnode
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n=n.ref
                if n==self.head:
                    break
            if n==self.head:
                raise Exception("Given Node value is not Present") 
            else:
                newnode = Node(data)
                newnode.ref = n.ref
                n.ref = newnode
    def del_first(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        elif self.head == self.tail:
            self.head=self.tail = None
        else:
            self.tail.ref = self.head.ref
            self.head = self.head.ref
    def del_last(self):
        if self.head is None:
            raise Exception("Linked List is empty")
        elif self.head == self.tail:
            self.head=self.tail = None
        else:
            n=self.head
            while n.ref is not None:
                n = n.ref
                if n.ref.ref==self.head:
                    break
            n.ref=self.head
            self.tail=n
    def del_by_val(self,x):
        if self.head is None:
            raise Exception("Linked List is empty")
        elif self.head == self.tail:
            if self.head.data==x:
                self.head=self.tail = None
        elif self.head.data==x:
            self.tail.ref = self.head.ref
            self.head = self.head.ref
        elif self.tail.data==x:
            n=self.head
            while n.ref is not None:
                n = n.ref
                if n.ref.ref==self.head:
                    break
            n.ref=self.head
            self.tail=n
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
                if n==self.head:
                    break
            if n.ref==self.head:
                raise Exception("Given Node value is not Present")
            else:
                n.ref = n.ref.ref
        
    def traversal(self):
        if self.head is None:
            return "Circular Linked List Is Empty"
        n = self.head
        while n is not None:
            print(n.data,end="-->")
            n = n.ref
            if n == self.head:
                break

                
cll = Circular_Linked_List()
cll.add_begin(10)
cll.add_begin(20)
cll.add_begin(80)
cll.add_end(30)
cll.add_end(40)
cll.add_after(40,70)
cll.add_before(80,90)
cll.del_first()
cll.del_last()
cll.del_by_val(20)
cll.traversal()


# ### Binary Search Tree

# In[87]:


class BST:
    def __init__(self,key=None):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if data<self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    def preorder(self):
        print(self.key,end="-->")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def postorder(self):
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
        print(self.key,end="-->")
    def inorder(self):
        if self.lchild:
            self.lchild.preorder()
        print(self.key,end="-->")
        if self.rchild:
            self.rchild.preorder()
    def search(self,x):
        if self.key == x:
            print("Node is present")
            return
        elif x<self.key:
            if self.lchild:
                self.lchild.search(x)
            else:
                print("Node is not present")
        elif x>self.key:
            if self.rchild:
                self.rchild.search(x)
            else:
                print("Node is not present")
    def min_ele(self):
        curr = self
        while curr.lchild:
            curr = curr.lchild
        print(curr.key)
    def max_ele(self):
        curr = self
        while curr.rchild:
            curr = curr.rchild
        print(curr.key)
root = BST()
for i in [1,10,2,34,54,68]:
    root.insert(i)  
root.preorder()
# root.postorder()
# root.inorder()
# root.search(68)
print()
root.min_ele()
root.max_ele()


# In[77]:





# In[78]:





# In[79]:


root.postorder()


# In[80]:


root.inorder()


# In[75]:


root.search(68)


# In[ ]:




