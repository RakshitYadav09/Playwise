# pinned_shuffle.py

import random

# this function marks a song as pinned so it doesn't move when shuffling
def mark_song_pinned(playlist, index):
    """
    Time Complexity: O(n), n = index
    Space Complexity: O(1)
    """
    current = playlist.head
    for _ in range(index):
        if current:
            current = current.next

    if current:
        current.pinned = True
        print(f"'{current.title}' has been pinned at position {index + 1}.")
    else:
        print("Invalid index. Cannot pin.")

# this function unpins a song so it becomes eligible for shuffling again
def unmark_song_pinned(playlist, index):
    """
    Time Complexity: O(n), n = index
    Space Complexity: O(1)
    """
    current = playlist.head
    for _ in range(index):
        if current:
            current = current.next

    if current:
        current.pinned = False
        print(f"'{current.title}' has been unpinned from position {index + 1}.")
    else:
        print("Invalid index. Cannot unpin.")

# this shuffles only unpinned songs while keeping pinned ones fixed in place
def shuffle_with_pins(playlist):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    current = playlist.head
    unpinned_nodes = []

    # collect all unpinned songs into a list
    while current:
        if not current.pinned:
            unpinned_nodes.append(current)
        current = current.next

    # if less than 2 unpinned songs, no need to shuffle
    if len(unpinned_nodes) < 2:
        print("Not enough unpinned songs to shuffle.")
        return

    # randomly shuffle the unpinned songs
    random.shuffle(unpinned_nodes)

    # reassign the shuffled data back to their original positions
    current = playlist.head
    i = 0
    while current:
        if not current.pinned:
            # assign data from shuffled list
            shuffled = unpinned_nodes[i]
            current.title = shuffled.title
            current.artist = shuffled.artist
            current.duration = shuffled.duration
            i += 1
        current = current.next

    print("Shuffling complete. Pinned songs were kept in place.")

# this menu lets the user interact with pin and shuffle options
def handle_shuffle_menu(playlist):
    while True:
        # Time Complexity: O(1) per menu operation (except pin/unpin/shuffle which depend on above methods)
        # Space Complexity: O(1)
        print("\n--- Shuffle Menu ---")
        print("1. Pin a Song")
        print("2. Unpin a Song")
        print("3. Shuffle Unpinned Songs")
        print("4. Display Playlist")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                index = int(input("Enter index of song to pin: ")) - 1
                mark_song_pinned(playlist, index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                index = int(input("Enter index of song to unpin: ")) - 1
                unmark_song_pinned(playlist, index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            shuffle_with_pins(playlist)

        elif choice == "4":
            playlist.display()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")
