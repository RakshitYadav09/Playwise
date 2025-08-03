# sort_utils.py

# this file contains the logic for sorting the playlist using Merge Sort or Quick Sort
# user can sort by either title or duration
# both sorting algorithms work on the doubly linked list used in the playlist

# ============================
# PUBLIC FUNCTION TO BE CALLED
# ============================

# this function performs sorting on the playlist using the selected algorithm and field
def sort_playlist(playlist, key='title', algorithm='merge'):
    """
    Time Complexity: O(n log n), n = number of songs
    Space Complexity: O(log n) for merge sort, O(log n) for quick sort (recursion stack)
    """
    if algorithm == 'merge':
        playlist.head = merge_sort(playlist.head, key)  # call merge sort
    elif algorithm == 'quick':
        playlist.head = quick_sort(playlist.head, key)  # call quick sort
    else:
        print("Invalid sorting algorithm.")
        return

    # after sorting we fix the prev pointers and update the tail
    current = playlist.head
    prev = None
    playlist.size = 0

    while current:
        current.prev = prev
        prev = current
        current = current.next
        playlist.size += 1

    playlist.tail = prev
    print(f"Playlist has been sorted by {key} using {algorithm} sort.")

# this function shows a menu for the user to choose how to sort the playlist
def handle_sort_menu(playlist):
    while True:
        # Time Complexity: O(1) per menu operation (except sort which depends on sort_playlist)
        # Space Complexity: O(1)
        print("\nSort Playlist")
        print("1. Sort by Title")
        print("2. Sort by Duration")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice in ["1", "2"]:
            key = 'title' if choice == "1" else 'duration'

            print("\nChoose Sorting Algorithm")
            print("1. Merge Sort")
            print("2. Quick Sort")
            algo_choice = input("Enter your choice: ")

            if algo_choice == "1":
                algorithm = 'merge'
            elif algo_choice == "2":
                algorithm = 'quick'
            else:
                print("Invalid algorithm choice.")
                continue

            sort_playlist(playlist, key=key, algorithm=algorithm)
            playlist.display()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

# ======================
# MERGE SORT IMPLEMENTATION
# ======================

# this is the recursive merge sort function
def merge_sort(head, key):
    """
    Time Complexity: O(n log n)
    Space Complexity: O(log n)
    """
    if head is None or head.next is None:
        return head

    # split the list into two halves
    left, right = split(head)

    # recursively sort each half
    left = merge_sort(left, key)
    right = merge_sort(right, key)

    # merge the sorted halves
    return merge_sorted_lists(left, right, key)

# this splits the linked list into two halves using the slow-fast pointer method
def split(head):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    slow = head
    fast = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    middle = slow.next
    slow.next = None
    if middle:
        middle.prev = None

    return head, middle

# this merges two sorted linked lists into one
def merge_sorted_lists(left, right, key):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not left:
        return right
    if not right:
        return left

    if compare(left, right, key):
        result = left
        result.next = merge_sorted_lists(left.next, right, key)
        if result.next:
            result.next.prev = result
        result.prev = None
    else:
        result = right
        result.next = merge_sorted_lists(left, right.next, key)
        if result.next:
            result.next.prev = result
        result.prev = None

    return result

# ======================
# QUICK SORT IMPLEMENTATION
# ======================

# this is the main quick sort function
def quick_sort(head, key):
    """
    Time Complexity: O(n log n) average, O(n^2) worst case
    Space Complexity: O(log n)
    """
    tail = last_node(head)
    quick_sort_recursive(head, tail, key)
    return head

# this is the recursive quick sort helper
def quick_sort_recursive(start, end, key):
    """
    Time Complexity: O(n log n) average, O(n^2) worst case
    Space Complexity: O(log n)
    """
    if not start or start == end or start == end.next:
        return

    # partition and get pivot
    pivot_node = partition(start, end, key)

    # recursively sort left and right halves
    if pivot_node and pivot_node.prev:
        quick_sort_recursive(start, pivot_node.prev, key)

    if pivot_node and pivot_node.next:
        quick_sort_recursive(pivot_node.next, end, key)

# this partitions the list and returns the pivot node
def partition(start, end, key):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    pivot = end
    i = start.prev
    j = start

    while j != end:
        if compare(j, pivot, key):
            i = i.next if i else start
            swap_node_data(i, j)
        j = j.next

    i = i.next if i else start
    swap_node_data(i, end)
    return i

# helper to find the last node in the list
def last_node(node):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    while node and node.next:
        node = node.next
    return node

# helper that swaps data of two nodes (doesn't change their links)
def swap_node_data(a, b):
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    a.title, b.title = b.title, a.title
    a.artist, b.artist = b.artist, a.artist
    a.duration, b.duration = b.duration, a.duration

# ======================
# COMPARISON LOGIC (COMMON FOR BOTH ALGORITHMS)
# ======================

# this compares two song nodes based on the selected key
def compare(a, b, key):
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if key == 'duration':
        return a.duration <= b.duration
    return a.title.lower() <= b.title.lower()
