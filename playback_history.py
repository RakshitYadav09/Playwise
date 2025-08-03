# playback_history.py

# first we define a class to manage the playback history using a stack
class PlaybackHistory:
    def __init__(self):
        self.stack = []  # stack to store recently played songs
# this function is called when a song is played
    def play_song(self, song):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.stack.append(song)  # push the song onto the stack
        print(f"🎧 Now playing: {song.title} by {song.artist}")

    # this function undoes the last played song and returns it
    def undo_last_play(self):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if not self.stack:
            print("⚠️ No recently played songs to undo.")
            return None

        # pop the last played song from the stack
        last_song = self.stack.pop()
        print(f"↩️ Undo last play: {last_song.title} by {last_song.artist}")
        return last_song

    # this function displays the current playback history
    def show_history(self):
        """
        Time Complexity: O(n), n = number of played songs
        Space Complexity: O(1)
        """
        print("\n📜 Recently Played Songs:")
        if not self.stack:
            print("No songs played yet.")
        else:
            # we print the songs in reverse because the last one played is on top
            for i, song in enumerate(reversed(self.stack), 1):
                print(f"{i}. {song.title} by {song.artist}")
                
    # this function provides a menu interface to interact with the playback stack
def handle_playback_history(playlist, history):
    while True:
        # Time Complexity: O(1) per menu operation (except play/show/undo which depend on PlaybackHistory methods)
        # Space Complexity: O(1)
        print("\n🎬 Playback History Options")
        print("1. Play a Song")
        print("2. Undo Last Played Song")
        print("3. Show Playback History")
        print("0. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            playlist.display()
            try:
                index = int(input("Enter index of song to play: ")) - 1
                current = playlist.head
                for _ in range(index):
                    if current:
                        current = current.next
                if current:
                    history.play_song(current)
                else:
                    print("❌ Invalid song index.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "2":
            last_song = history.undo_last_play()
            if not last_song:
                print("No song to undo.")

        elif choice == "3":
            history.show_history()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")
