class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


def deleteSpecificNode(head, nodeToDelete):  # (node1, node4)
    if head == nodeToDelete:  # node1 == node4 : False
        return head.next  # skip

    currentNode = head  # currentNode = node1
    while currentNode.next and currentNode.next != nodeToDelete:
        # node2 and node2 != node4 : True
        # node3 and node3 != node4 : True
        # node3 and node4 != node4 : False, stop loop
        currentNode = currentNode.next  # currentNode = node2 -> node3

    if currentNode.next is None:  # node3 is None : False
        return head  # skip

    currentNode.next = currentNode.next.next  # node3 = node5

    return head  # return


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)  # traverse through the linked list normally

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)  # traverse after deleting a node
