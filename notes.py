"""
notes.py — sorting, searching, and linked lists.

Order is easy -> hard:
    1. Selection sort
    2. Insertion sort
    3. Merge sort
    4. Binary search
    5. Singly linked list
    6. Doubly linked list

All sort functions return a NEW list and leave the input untouched.
"""


# ---------------------------------------------------------------------------
# 1. SELECTION SORT                                    O(n^2) time, O(1) extra
# ---------------------------------------------------------------------------
# Idea: the array is split into a sorted prefix and an unsorted suffix.
# On each pass you find the smallest element in the suffix and swap it into
# the first slot of the suffix, so the sorted prefix grows by one.
#
#   [ sorted | unsorted ]
#              ^ find min here, swap it to the front of this part

def selection_sort(arr):
    arr = arr[:]                      # copy, so the caller's list is safe
    n = len(arr)

    for i in range(n):
        # Assume the element at i is the smallest, then look for a smaller one.
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Put the true minimum at position i.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# ---------------------------------------------------------------------------
# 2. INSERTION SORT                        O(n^2) worst, O(n) best, O(1) extra
# ---------------------------------------------------------------------------
# Idea: like sorting playing cards in your hand. arr[0..i-1] is already
# sorted. Take arr[i] ("key"), slide every bigger element one step right,
# then drop the key into the hole that opens up.
#
# Fast on nearly-sorted data because the inner while loop barely runs.

def insertion_sort(arr):
    arr = arr[:]

    for i in range(1, len(arr)):
        key = arr[i]                  # the element we are placing
        j = i - 1                      # last index of the sorted part

        # Shift everything greater than key one position to the right.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # j is now either -1 or points at an element <= key,
        # so the correct slot for key is j + 1.
        arr[j + 1] = key

    return arr


# ---------------------------------------------------------------------------
# 3. MERGE SORT                                   O(n log n) time, O(n) extra
# ---------------------------------------------------------------------------
# Divide and conquer:
#   split the list in half -> sort each half -> merge the two sorted halves.
# The real work happens in merge().

def merge(left, right):
    """Combine two already-sorted lists into one sorted list."""
    i = j = 0
    merged = []
    n1, n2 = len(left), len(right)

    # Repeatedly take the smaller of the two front elements.
    while i < n1 and j < n2:
        if left[i] <= right[j]:       # '<=' keeps the sort stable
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # One list is now empty; the other's remaining tail is already sorted.
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(array):
    """Recursive merge sort. Returns a new sorted list."""
    n = len(array)
    if n <= 1:                        # base case: 0 or 1 element is sorted
        return array[:]

    mid = n // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


# ---------------------------------------------------------------------------
# 4. BINARY SEARCH                                  O(log n), sorted input only
# ---------------------------------------------------------------------------
# Keep a window [lo, hi] that must contain the target if it exists.
# Compare with the middle element and throw away half the window each step.
# Returns the index of target, or -1 if it is not there.

def binary_search(arr, target):
    """Iterative version."""
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        # 'lo + (hi - lo) // 2' instead of '(lo + hi) // 2' avoids overflow in
        # languages with fixed-size ints. In Python both are fine, but keep
        # the habit for C++/Java.
        mid = lo + (hi - lo) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1              # target must be in the left half
        else:
            lo = mid + 1              # target must be in the right half

    return -1                          # window became empty


def binary_search_rec(arr, lo, hi, target):
    """Recursive version. Call as binary_search_rec(arr, 0, len(arr)-1, x)."""
    if lo > hi:                       # empty window -> not found
        return -1

    mid = lo + (hi - lo) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_rec(arr, lo, mid - 1, target)
    else:
        return binary_search_rec(arr, mid + 1, hi, target)


# ---------------------------------------------------------------------------
# 5. SINGLY LINKED LIST
# ---------------------------------------------------------------------------
# A Python list stores elements side by side in memory, so arr[i] is instant.
# A linked list stores each value in its own Node, and each node holds a
# pointer to the next one. There is no indexing — to reach position i you
# must walk i steps from the head.
#
#   _head -> [10 | *] -> [20 | *] -> [30 | None] <- _tail
#
# Why bother: inserting or deleting in the middle is just pointer rewiring,
# no shifting of elements like a Python list does.
#
# The class keeps three pieces of state, and every method must keep all three
# consistent:
#   _head : first node (None if empty)
#   _tail : last node  (None if empty)  -> makes append O(1)
#   _n    : number of elements          -> makes length() O(1)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next              # pointer to the next Node, or None


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._n = 0

    # -- basics ------------------------------------------------------------
    def length(self):
        return self._n

    def __len__(self):                # lets you write len(my_list)
        return self._n

    def _node_at(self, i):
        """Return the node at index i. O(i) — this is the price of a list
        with no indexing. Leading underscore = internal helper."""
        if not 0 <= i < self._n:
            raise IndexError(f"index {i} out of range for length {self._n}")

        node = self._head
        for _ in range(i):            # take i steps forward
            node = node.next
        return node

    def get(self, i):
        return self._node_at(i).value

    def set(self, i, x):
        self._node_at(i).value = x

    # -- insertion ---------------------------------------------------------
    def insert(self, i, x):
        """Insert x so that it ends up at index i.
        Valid i: 0 .. _n (i == _n means 'append at the end').

        Three cases, because the head and the tail pointers need care:
          i == 0    -> new node becomes the head
          i == _n   -> new node becomes the tail  (O(1), thanks to _tail)
          otherwise -> rewire the node at i-1     (O(i))
        """
        if not 0 <= i <= self._n:
            raise IndexError(f"cannot insert at {i} in a list of length {self._n}")

        if i == 0:
            self._head = Node(x, self._head)
            if self._n == 0:          # list was empty: head is also the tail
                self._tail = self._head

        elif i == self._n:
            self._tail.next = Node(x)
            self._tail = self._tail.next

        else:
            prev = self._node_at(i - 1)
            # new node points to whatever prev used to point to,
            # then prev points to the new node. Order matters.
            prev.next = Node(x, prev.next)

        self._n += 1

    def append(self, x):
        self.insert(self._n, x)

    # -- deletion ----------------------------------------------------------
    def delete(self, i):
        """Remove the element at index i."""
        if not 0 <= i < self._n:
            raise IndexError(f"index {i} out of range for length {self._n}")

        if i == 0:
            self._head = self._head.next
            if self._head is None:    # list became empty
                self._tail = None
        else:
            prev = self._node_at(i - 1)
            removed = prev.next
            prev.next = removed.next  # skip over 'removed'
            if removed is self._tail: # we deleted the last node
                self._tail = prev

        self._n -= 1

    # -- convenience -------------------------------------------------------
    def to_list(self):
        """Walk the whole chain and collect values. Handy for debugging."""
        out, node = [], self._head
        while node is not None:
            out.append(node.value)
            node = node.next
        return out

    def __repr__(self):
        return f"LinkedList({self.to_list()})"


# ---------------------------------------------------------------------------
# 6. DOUBLY LINKED LIST
# ---------------------------------------------------------------------------
# Same idea, but every node also points backwards:
#
#   None <- [10] <-> [20] <-> [30] -> None
#
# The extra 'prev' pointer buys you two things:
#   - you can walk backwards, so reaching index i can start from whichever
#     end is closer (still O(n), but roughly half the steps)
#   - given a node, you can delete it without knowing its predecessor
#
# The cost: every insert/delete has to fix two pointers instead of one, and
# forgetting one of them is the classic bug.

class DNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._n = 0

    def length(self):
        return self._n

    def __len__(self):
        return self._n

    def _node_at(self, i):
        """Walk from the nearer end."""
        if not 0 <= i < self._n:
            raise IndexError(f"index {i} out of range for length {self._n}")

        if i <= self._n // 2:
            node = self._head
            for _ in range(i):
                node = node.next
        else:
            node = self._tail
            for _ in range(self._n - 1 - i):
                node = node.prev
        return node

    def get(self, i):
        return self._node_at(i).value

    def set(self, i, x):
        self._node_at(i).value = x

    def insert(self, i, x):
        if not 0 <= i <= self._n:
            raise IndexError(f"cannot insert at {i} in a list of length {self._n}")

        if self._n == 0:                       # empty list
            self._head = self._tail = DNode(x)

        elif i == 0:                           # new head
            node = DNode(x, None, self._head)
            self._head.prev = node
            self._head = node

        elif i == self._n:                     # new tail
            node = DNode(x, self._tail, None)
            self._tail.next = node
            self._tail = node

        else:                                  # somewhere in the middle
            nxt = self._node_at(i)             # node currently at i
            prv = nxt.prev
            node = DNode(x, prv, nxt)
            prv.next = node                    # fix the four pointers
            nxt.prev = node

        self._n += 1

    def append(self, x):
        self.insert(self._n, x)

    def delete(self, i):
        node = self._node_at(i)                # raises if i is invalid

        # Detach 'node' by making its neighbours point at each other.
        # A missing neighbour means node was the head or the tail.
        if node.prev is None:
            self._head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self._tail = node.prev
        else:
            node.next.prev = node.prev

        self._n -= 1

    def to_list(self):
        out, node = [], self._head
        while node is not None:
            out.append(node.value)
            node = node.next
        return out

    def __repr__(self):
        return f"DoublyLinkedList({self.to_list()})"


# ---------------------------------------------------------------------------
# Quick self-test — runs only when you execute this file directly.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6, 0, -3]

    assert selection_sort(data) == sorted(data)
    assert insertion_sort(data) == sorted(data)
    assert merge_sort(data) == sorted(data)
    assert data == [5, 2, 9, 1, 5, 6, 0, -3]      # input untouched

    ordered = sorted(data)
    assert binary_search(ordered, 100) == -1

    ll = LinkedList()
    for v in [1, 2, 3]:
        ll.append(v)
    ll.insert(0, 0)          # front
    ll.insert(2, 99)         # middle
    assert ll.to_list() == [0, 1, 99, 2, 3]
    ll.delete(4)             # tail — _tail must move back
    ll.delete(0)             # head
    assert ll.to_list() == [1, 99, 2]
    ll.append(7)             # still works after deleting the old tail
    assert ll.to_list() == [1, 99, 2, 7]

    dll = DoublyLinkedList()
    for v in [1, 2, 3]:
        dll.append(v)
    dll.insert(1, 42)
    assert dll.to_list() == [1, 42, 2, 3]
    dll.delete(0)
    dll.delete(len(dll) - 1)
    assert dll.to_list() == [42, 2]

    print("all checks passed")
