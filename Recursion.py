# Move items to the end of the list
# define move_to_end() here
def move_to_end(lst, val):
  if len(lst) == 0:
    return []
  if lst[0] == val:
    return move_to_end(lst[1:], val) + [lst[0]]
  else:
    return [lst[0]] + move_to_end(lst[1:], val)


# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))

# -----------------------------------------------------------------------------------------
# Delete i-th node from a linked list
import LinkedList

# Definition for singly-linked list node.
# class ListNode:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

# define remove_node() here
def remove_node(head, i):
  if i < 0:
    return head
  if head == None:
    return None
  if i == 0:
    return head.next_node
  #print(head.value)
  #print(head.next_node.value)
  head.next_node = remove_node(head.next_node, i - 1)
  return head
  #print(head.next_node.value)
  

# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 3)
print(head.flatten())

# -----------------------------------------------------------------------------------------
#Prepend and append to a string
# define wrap_string() here
def wrap_string(str, n):
  if n == 0:
    return str
  result = wrap_string(str, n - 1)
  return f"<{result}>"

# Test code - do not edit
wrapped = wrap_string("Pearl", 3)
print(wrapped)
