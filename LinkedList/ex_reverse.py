from LinkedList.ListNode import ListNode

if __name__ == "__main__":
  pass

def ll_print(root):
  while root:
    print(root.val)
    root = root.next

def createNested():
  root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
  return root

def reverse(head):
  if not head or not head.next:
    return head

  curr = head
  prev = None
  next = None
  while (curr):
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

  return prev

def showReverse():
  head = createNested()
  ll_print(head)

  head = reverse(head)
  ll_print(head)
