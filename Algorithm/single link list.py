class Node(object):
    def __init__(self,value):
        self.value=value
        self.newnode=None

# a=Node(5)
# b=Node(4)
# c=Node(9)
# d=Node(8)

# a.newnode=b
# b.newnode=c
# c.newnode=d
# print(a.value)
# print(a.newnode.newnode.newnode.value)

def Single_Link_list_cycle_check(node):
    marker1=node
    marker2=node

    while marker2!=None and marker2.newnode!=None:
        marker1=marker1.newnode
        marker2=marker2.newnode.newnode

        if marker1==marker2:
            return True
    return False

        #here we make cyclic so we get true 
# a=Node(5)
# b=Node(4)
# c=Node(9)
# a.newnode=b
# b.newnode=c
# c.newnode=a

# print(Single_Link_list_cycle_check(a))



class DoubleLinkList(object):

    def __init__(self,value):
        self.value=value
        self.next_node=None
        self.prev_node=None

# a=DoubleLinkList(6)
# b=DoubleLinkList(4)
# c=DoubleLinkList(5)

 # a.next_node=b
# b.prev_node=a
# print(a.value)
# print(a.next_node.value)
# print(b.prev_node.value)
