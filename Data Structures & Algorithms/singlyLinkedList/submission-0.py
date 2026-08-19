class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        count = 0

        while curr and count < index:
            curr = curr.next
            count += 1
        if curr:
            return curr.val
        return -1
        

    def insertHead(self, val: int) -> None:
        newnode = ListNode(val)

        newnode.next = self.head.next
        self.head.next = newnode

        if not newnode.next:
            self.tail = newnode

    def insertTail(self, val: int) -> None:
        newnode = ListNode(val)

        self.tail.next = newnode
        self.tail = newnode
        
    def remove(self, index: int) -> bool:
        count = 0
        curr = self.head

        while curr and count < index:
            curr = curr.next
            count += 1
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        vals = []
        while curr:
            vals += [curr.val]
            curr = curr.next
        return vals
        
