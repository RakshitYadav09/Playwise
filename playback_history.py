# playback_history.py

# first we define a class to manage the playback history using a stack
class PlaybackHistory:
    def __init__(self):
        self.stack = []  # stack to store recently played songs
# this function is called when a song is played
    def play_song(self, song):
        self.stack.append(song)  # push the song onto the stack
        print(f"🎧 Now playing: {song.title} by {song.artist}")

    # this function undoes the last played song and returns it
    def undo_last_play(self):
        if not self.stack:
            print("⚠️ No recently played songs to undo.")
            return None

        # pop the last played song from the stack
        last_song = self.stack.pop()
        print(f"↩️ Undo last play: {last_song.title} by {last_song.artist}")
        return last_song

    # this function displays the current playback history
    def show_history(self):
        print("\n📜 Recently Played Songs:")
        if not self.stack:
            print("No songs played yet.")
        else:
            # we print the songs in reverse because the last one played is on top
            for i, song in enumerate(reversed(self.stack), 1):
                print(f"{i}. {song.title} by {song.artist}")