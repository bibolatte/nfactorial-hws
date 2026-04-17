from typing import List, Any, Dict, Set, Generator

class StaticArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        self.capacity = capacity
        self.array = [None] * capacity

    def set(self, index: int, value: int) -> None:
        if index < 0 or index >= self.capacity:
            raise IndexError
        
        self.array[index] = value

    def get(self, index: int) -> int:
        if index < 0 or index > self.capacity:
            raise IndexError
        return self.array[index]



class DynamicArray:
    def __init__(self):
        self.array = []

    def append(self, value: int) -> None:
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        if index < 0 or index > len(self.array):
            raise IndexError
        self.array.insert(value)

    def delete(self, index: int) -> None:
        if index < 0 or index > len(self.array):
            raise IndexError
        self.array.pop(index)

    def get(self, index: int) -> int:
        return self.array(index)



class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def insert(self, position: int, value: int) -> None:
        if position < 0 or position > self.length:
            raise IndexError
        
        new_node = Node(value)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self._size == 0:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            
            if new_node.next is None:
                self.tail = new_node
        
        self._size += 1

    def delete(self, value: int) -> None:
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        if current.next is not None:
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            self._size -= 1

    def find(self, value: int) -> Node:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.head is None

    def print_list(self) -> None:
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")
    
    def reverse(self) -> None:
        if self.head is None or self.head.next is None:
            return
        
        prev = None
        current = self.head
        self.tail = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def get_head(self) -> Node:
        return self.head
    
    def get_tail(self) -> Node:
        return self.tail
    


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, value: int) -> None:
        """Add a node with a value to the end of the linked list."""
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def insert(self, position: int, value: int) -> None:
        """Insert a node with a value at a particular position."""
        if position < 0 or position > self._size:
            raise IndexError("Position out of range")
        
        new_node = Node(value)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self._size == 0:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            
            if new_node.next is None:
                self.tail = new_node
        
        self._size += 1
    
    def delete(self, value: int) -> None:
        """Delete the first node with a specific value."""
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return
        
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        if current.next is not None:
            current.next = current.next.next
            if current.next is None:
                self.tail = current
            self._size -= 1
    
    def find(self, value: int) -> Optional[Node]:
        """Find a node with a specific value."""
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def size(self) -> int:
        """Returns the number of elements in the linked list."""
        return self._size
    
    def is_empty(self) -> bool:
        """Checks if the linked list is empty."""
        return self.head is None
    
    def print_list(self) -> None:
        """Prints all elements in the linked list."""
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")
    
    def reverse(self) -> None:
        """Reverse the linked list in-place."""
        if self.head is None or self.head.next is None:
            return
        
        prev = None
        current = self.head
        self.tail = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def get_head(self) -> Optional[Node]:
        """Returns the head node of the linked list."""
        return self.head
    
    def get_tail(self) -> Optional[Node]:
        """Returns the tail node of the linked list."""
        return self.tail


class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value: int) -> None:
        new_node = DoubleNode(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self._size += 1

    def insert(self, position: int, value: int) -> None:
        if position < 0 or position > self._size:
            raise IndexError("Position out of range")
        
        new_node = DoubleNode(value)
        
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self._size == 0:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            
            new_node.next = current.next
            new_node.prev = current
            
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            
            if new_node.next is None:
                self.tail = new_node
        
        self._size += 1

    def delete(self, value: int) -> None:
        if self.head is None:
            return
        
        current = self.head
        while current and current.value != value:
            current = current.next
        
        if current is None:
            return
        
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        
        self._size -= 1

    def find(self, value: int) -> Any:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.head is None

    def print_list(self) -> None:
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" <-> ".join(elements) if elements else "Empty list")

    def reverse(self) -> None:
        if self.head is None or self.head.next is None:
            return
        
        current = self.head
        self.tail = self.head
        
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        
        self.head, self.tail = self.tail, self.head

    def get_head(self) -> Any:
        return self.head

    def get_tail(self) -> Any:
        return self.tail
    

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value: int) -> None:
        self.data.append(value)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self.data.pop(0)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Cannot peek at empty queue")
        return self.data[0]

    def is_empty(self) -> bool:
        return len(self.data) == 0
    


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value: int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def preorder_traversal(self) -> List[int]:
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node: TreeNode, result: List[int]) -> None:
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder_traversal(self) -> List[int]:
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node: TreeNode, result: List[int]) -> None:
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

    def level_order_traversal(self) -> List[int]:
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result

    def minimum(self) -> Any:
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current

    def maximum(self) -> Any:
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current

    def is_valid_bst(self) -> bool:
        return self._is_valid_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_recursive(self, node: TreeNode, min_val: float, max_val: float) -> bool:
        if node is None:
            return True
        if node.value <= min_val or node.value >= max_val:
            return False
        return (self._is_valid_recursive(node.left, min_val, node.value) and
                self._is_valid_recursive(node.right, node.value, max_val))



def insertion_sort(lst: List[int]) -> List[int]:
    arr = lst.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(lst: List[int]) -> List[int]:
    arr = lst.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort(lst: List[int]) -> List[int]:
    arr = lst.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def shell_sort(lst: List[int]) -> List[int]:
    arr = lst.copy()
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst.copy()
    
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst.copy()
    
    arr = lst.copy()
    _quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_recursive(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort_recursive(arr, low, pi - 1)
        _quick_sort_recursive(arr, pi + 1, high)


def _partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1