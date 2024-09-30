class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None


    def insert(self, value):

        #create new node
        newNode = Node(value)

        if self.head is None: #if its a first node
            self.head = newNode
        else:
            temp = self.head #if not, point the next pointer to the new node
            while temp.next is not None:
                temp = temp.next

            temp.next = newNode

        return
    
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete(self, value):

        temp = self.head

        if temp is not None and temp.data == value: #its a head node
            self.head = temp.next
            del temp
            return
        
        previousNode=None #node preioud to the node to be deleted
        while temp:
            if temp.data == value:
                break
                
            previousNode = temp   
            temp = temp.next  

        if temp is Node: #that means it reasched the end of linked list
            print("Node not found")
            return    

        previousNode.next = temp.next     
        temp = None 

        return    

linkedlist = LinkedList()

linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(4)

linkedlist.traverse()

linkedlist.delete(3)
linkedlist.traverse()

