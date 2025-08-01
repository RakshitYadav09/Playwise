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
        self.head = None                    # First song in the playlist the head keeps track of first song
        self.tail = None                    # Last song in the playlist the tail keeps track of last song
        self.name = name                    # Name of the playlist
        self.size = 0                       # Number of songs in the playlist

    # helper function to convert "mm:ss" string to seconds
    def _parse_duration(self, duration_str):
        try:
            minutes, seconds = map(int, duration_str.split(":"))
            return minutes * 60 + seconds
        except Exception:
            print("Invalid duration format. Use mm:ss (e.g., 1:30).")
            return 0

    # helper function to convert seconds to "mm:ss" string
    def _format_duration(self, seconds):
        minutes = seconds // 60
        sec = seconds % 60
        return f"{minutes}:{sec:02d}"

    # this adds a new song to the end of the playlist
    def add_song(self, title, artist, duration):
        duration_sec = self._parse_duration(duration)  # convert "mm:ss" to seconds
        if duration_sec == 0:
            return  # invalid format, do not add the song

        new_node = SongNode(title, artist, duration_sec)

        # if the playlist is empty we add the new song as both head and tail
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # link new node to end of list
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1
        print(f"✅ Added: {title} by {artist} to '{self.name}' ({self._format_duration(duration_sec)})")

    # this deletes the song at a given index
    def delete_song(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index. No song deleted.")
            return

        # start from beginning of the playlist
        current = self.head

        # move to the node at the given index
        for _ in range(index):
            current = current.next

        # now we need to unlink this node from the list and delete the song 

        #if the song is not the first song
        if current.prev:
            current.prev.next = current.next
        else:  
            self.head = current.next # we are deleting the head, so move head to next song

        # if the song is not the last song 
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev # we are deleting the tail, so move tail to previous song

        self.size -= 1
        print(f"Deleted song: {current.title} by {current.artist} from '{self.name}'.")

    # this moves a song from one index to another
    def move_song(self, from_index, to_index):
        if from_index == to_index:
            print("Song is already at the desired position.")
            return
        if from_index < 0 or from_index >= self.size or to_index < 0 or to_index >= self.size:
            print("Invalid indices, cannot move song.")
            return
        # find the song to move
        current = self.head
        for _ in range(from_index):
            current = current.next

        # unlink the song from its current place
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev 

        # insert current at to_index
        if to_index == 0:
            current.next = self.head # move to the beginning
            if self.head:
                self.head.prev = current
            current.prev = None
            self.head = current
        else:
            temp = self.head 

            for _ in range(to_index - 1): # move to the middle or ending 
                temp = temp.next

            current.next = temp.next # link current to the next song
            if temp.next:
                temp.next.prev = current
            current.prev = temp
            temp.next = current

            # if inserted at the end, update tail
            if current.next is None:
                self.tail = current
        print(f"Moved song: {current.title} by {current.artist} to {to_index} in '{self.name}'.")

    # this reverses the order of the entire playlist
    def reverse_playlist(self):
        current = self.head
        prev = None

        # we will make old head become the new tail
        self.tail = self.head

         # go through the playlist and swap next and prev for each node
        while current:
            next_node = current.next  # store next node temporarily
            current.next = current.prev  # swap next and prev
            current.prev = next_node
            prev = current
            current = next_node  # move to the next node in original order

         # now set the new head of the reversed list
        self.head = prev
        print("Playlist reversed")

    # this displays the full playlist in order
    def display(self):
        current = self.head
        print(f"\nPlaylist: {self.name}")
        print("-" * 40)

        index = 1  # CHANGED: Start numbering from 1
        while current:
            print(f"{index}. {current.title} by {current.artist} ({self._format_duration(current.duration)})")  # CHANGED: show duration as "mm:ss"
            current = current.next
            index += 1
        print("-" * 40)
        print(f"Total songs in your Playlist: {self.size}")