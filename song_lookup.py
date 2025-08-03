# song_lookup.py

# this class uses a dictionary (hash map) to store and find songs instantly by title
class SongLookup:
    def __init__(self):
        self.song_map = {}  # internal dictionary to map song title to song node

    # this adds a song to the hash map using its title as the key
    def add_song(self, song):
        """
        Adds a song to the lookup map (case-insensitive).
        Handles edge cases: ignores None, empty title, and avoids duplicates.
        """
        if not song or not getattr(song, 'title', None):
            print("❌ Invalid song object or missing title.")
            return
        key = song.title.strip().lower()
        if key in self.song_map:
            print(f"⚠️ Song '{song.title}' already exists in lookup.")
        else:
            self.song_map[key] = song
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if song.title in self.song_map:
            print(f"⚠️ Song '{song.title}' already exists in lookup.")
        else:
            self.song_map[song.title] = song

    # this searches for a song by title and shows its info
    def find_song(self, title):
        """
        Finds a song by title (case-insensitive).
        Handles edge cases: trims whitespace, checks for empty input.
        """
        if not title or not title.strip():
            print("❌ Please enter a valid song title.")
            return
        key = title.strip().lower()
        song = self.song_map.get(key)
        if song:
            print(f"\n🔍 Found Song: {song.title}")
            print(f"Artist: {song.artist}")
            print(f"Duration: {song.duration // 60}:{song.duration % 60:02d}")
        else:
            print(f"❌ No song found with title '{title}'.")
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        song = self.song_map.get(title)
        if song:
            print(f"\n🔍 Found Song: {song.title}")
            print(f"Artist: {song.artist}")
            print(f"Duration: {song.duration // 60}:{song.duration % 60:02d}")
        else:
            print(f"❌ No song found with title '{title}'.")

    # this deletes a song from the lookup table by title (optional)
    def delete_song(self, title):
        """
        Deletes a song by title (case-insensitive).
        Handles edge cases: trims whitespace, checks for empty input.
        """
        if not title or not title.strip():
            print("❌ Please enter a valid song title.")
            return
        key = title.strip().lower()
        if key in self.song_map:
            del self.song_map[key]
            print(f"🗑️ Deleted '{title}' from lookup.")
        else:
            print(f"❌ Song '{title}' not found in lookup.")
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if title in self.song_map:
            del self.song_map[title]
            print(f"🗑️ Deleted '{title}' from lookup.")
        else:
            print(f"❌ Song '{title}' not found in lookup.")

# this function gives a terminal interface for searching songs by title
def handle_song_lookup(lookup):
    while True:
        # Time Complexity: O(1) per menu operation (except search/delete which depend on SongLookup methods)
        # Space Complexity: O(1)
        print("\n🔎 Instant Song Lookup Menu")
        print("1. Search Song by Title")
        print("2. Delete Song from Lookup")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter song title to search: ")
            lookup.find_song(title)

        elif choice == "2":
            title = input("Enter song title to delete: ")
            lookup.delete_song(title)

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")
