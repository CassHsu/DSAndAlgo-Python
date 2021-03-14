from LinkedList.ListNode import ListNode

if __name__ == "__main__":
  pass

def ll_print(root):
  while root:
    print(root.val)
    root = root.next

def createNested():
  root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
  ll_print(root)

  