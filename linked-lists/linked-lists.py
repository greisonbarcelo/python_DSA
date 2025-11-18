class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverseAndPrint(head):
    currentNode = head  # currentNode = node1 = 7
    while currentNode:  # while currentNode is not None/Null print the data
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next  # after printing currentNode, move to the next node
    # triggers once it reaches the tail of the node and nothing after it
    print("null")


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# calls the 'head' of the node list in traverseAndPrint function
traverseAndPrint(node1)
