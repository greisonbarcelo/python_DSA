class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findLowestValue(head):
    minValue = head.data  # minValue = 7
    currentNode = head.next  # currentNode = node2
    while currentNode:  # node2->node3->node4->node5->stop
        if currentNode.data < minValue:  # if 11 < 7 : f -> 3 < 7 : t -> 2 < 3 : t -> 9 < 2 : f
            minValue = currentNode.data  # skip -> minValue = 3 -> minValue = 2 -> skip
        currentNode = currentNode.next  # currentNode = node3 -> node4 -> node5 -> None
    return minValue  # minValue = 2


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", findLowestValue(node1))
# The lowest value in the linked list is: 2
