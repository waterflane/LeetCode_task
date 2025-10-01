class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    def reversal(self):
        last = None
        now = self
        next = None
        while True:
            next = now.next
            now.next = last
            last = now
            now = next
            if now == None:
                return last
    def make_num(self):
        num_str = ''
        now = self
        while True:
            num_str += str(now.val)
            now = now.next
            if now == None:
                return num_str

    l1_num = make_num(reversal(l1))
    l2_num = make_num(reversal(l2))
    res = int(l1_num) + int(l2_num)
    res = list(str(res))

    now = ListNode(int(res[-1]), None)
    res.pop()

    while True:
        if res == []:
            return reversal(now)
        next = ListNode(int(res[-1]), now)
        now = next
        res.pop()
    
a3 = ListNode(3, None)
a2 = ListNode(4, a3)
a1 = ListNode(2, a2)

b3 = ListNode(4, None)
b2 = ListNode(6, b3)
b1 = ListNode(5, b2)

print(addTwoNumbers(a1, b1).val)
