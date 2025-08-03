# playlist_engine.py

# first we define the structure of a single song node in a doubly linked list
class SongNode:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # duration stored as seconds
        self.prev = None
        self.next = None

# then we define the structure of the playlist itself which is a doubly linked list
class Playlist:
    def __init__(self, name="My Playlist"):
        self.head = None         # points to the first song
        self.tail = None         # points to the last song
        self.name = name         # name of the playlist
        self.size = 0            # number of songs in the playlist

    # helper function to convert "mm:ss" string to seconds
    def _parse_duration(self, duration_str):
        try:
            minutes, seconds = map(int, duration_str.strip().split(":"))
            return minutes * 60 + seconds
        except Exception:
            print("❌ Invalid duration format. Use mm:ss (e.g., 1:30).")
            return 0

    # helper function to convert seconds to "mm:ss" string
    def _format_duration(self, seconds):
        minutes = seconds // 60
        sec = seconds % 60
        return f"{minutes}:{sec:02d}"

    # this adds a new song to the end of the playlist
    def add_song(self, title, artist, duration):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        duration_sec = self._parse_duration(duration)  # convert "mm:ss" to seconds
        if duration_sec == 0:
            return  # invalid format, skip adding

        new_node = SongNode(title, artist, duration_sec)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1
        print(f"✅ Added: {title} by {artist} to '{self.name}' ({self._format_duration(duration_sec)})")

    # deletes the song at a given index (0-based)
    def delete_song(self, index):
        """
        Time Complexity: O(n), n = index (worst case: delete last song)
        Space Complexity: O(1)
        """
        if index < 0 or index >= self.size:
            print("❌ Invalid index. No song deleted.")
            return

        current = self.head
        for _ in range(index):
            current = current.next

        # unlink the node
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next  # deleting the head

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev  # deleting the tail

        self.size -= 1
        print(f"🗑️ Deleted song: {current.title} by {current.artist} from '{self.name}'.")

    # moves a song from one index to another
    def move_song(self, from_index, to_index):
        """
        Time Complexity: O(n), n = max(from_index, to_index)
        Space Complexity: O(1)
        """
        if from_index == to_index:
            print("ℹ️ Song is already at the desired position.")
            return
        if from_index < 0 or from_index >= self.size or to_index < 0 or to_index >= self.size:
            print("❌ Invalid indices. Cannot move song.")
            return

        # locate the node to move
        current = self.head
        for _ in range(from_index):
            current = current.next

        # unlink the node from its current position
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

        # reinsert at the new position
        if to_index == 0:
            current.next = self.head
            current.prev = None
            if self.head:
                self.head.prev = current # pyright: ignore[reportAttributeAccessIssue]
            self.head = current
        else:
            temp = self.head
            for _ in range(to_index - 1):
                temp = temp.next

            current.next = temp.next
            current.prev = temp
            if temp.next:
                temp.next.prev = current
            temp.next = current

            if current.next is None:
                self.tail = current

        print(f"🔀 Moved: {current.title} by {current.artist} to position {to_index + 1}")

    # reverses the entire playlist
    def reverse_playlist(self):
        """
        Time Complexity: O(n), n = number of songs
        Space Complexity: O(1)
        """
        current = self.head
        prev = None
        self.tail = self.head  # the old head becomes the new tail

        while current:
            next_node = current.next
            current.next = current.prev
            current.prev = next_node
            prev = current
            current = next_node

        self.head = prev
        print("🔁 Playlist reversed.")

    # prints the full playlist
    def display(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        current = self.head
        print(f"\n🎵 Playlist: {self.name}")
        print("-" * 40)
        index = 1
        while current:
            print(f"{index}. {current.title} by {current.artist} ({self._format_duration(current.duration)})")
            current = current.next
            index += 1
        print("-" * 40)
        print(f"Total songs: {self.size}")

# this function gives a terminal menu for working with the playlist
# note: you can pass `lookup` object if you want to sync new songs into hash map
def handle_playlist_operations(playlist, lookup=None):
    while True:
        # Time Complexity: O(1) per menu operation (except add/delete/move/reverse which depend on Playlist methods)
        # Space Complexity: O(1)
        print("\n🎶 Playlist Operations 🎶")
        print("1. Add Song")
        print("2. Delete Song")
        print("3. Move Song")
        print("4. Reverse Playlist")
        print("5. Display Playlist")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            duration = input("Enter duration (mm:ss): ")
            playlist.add_song(title, artist, duration)

            # auto-sync new song to lookup map (optional)
            if lookup:
                new_song = playlist.tail
                lookup.add_song(new_song)

        elif choice == "2":
            try:
                index = int(input("Enter index of song to delete: "))
                playlist.delete_song(index - 1)
            except ValueError:
                print("❌ Please enter a valid index.")

        elif choice == "3":
            try:
                from_index = int(input("Enter current index of song: ")) - 1
                to_index = int(input("Enter new index to move it to: ")) - 1
                playlist.move_song(from_index, to_index)
            except ValueError:
                print("❌ Please enter valid indices.")

        elif choice == "4":
            playlist.reverse_playlist()

        elif choice == "5":
            playlist.display()

        elif choice == "0":
            break

        else:
            print("❌ Invalid choice. Try again.")
