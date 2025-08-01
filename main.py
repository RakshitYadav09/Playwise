from playlist_engine import Playlist
from playback_history import PlaybackHistory

# this function displays the main menu with all module options
def show_main_menu():
    print("\n🎵 Welcome to PlayWise Smart Music Engine 🎵")
    print("========== MAIN MENU ==========")
    print("1. Playlist Operations")
    print("2. Playback History (Play / Undo Last Played Song)")
    print("3. Song Rating (BST-based Recommendations)")
    print("4. Instant Song Lookup (Hash Map)")
    print("5. Sort Playlist (Merge/Quick Sort)")
    print("6. Export Live Dashboard Snapshot")
    print("7. Shuffle with Pinned Songs")
    print("8. Generate Playlist Summary Report")
    print("0. Exit")
    print("=================================")

# this function shows the playlist-related actions
def show_playlist_menu():
    print("\n🎶 Playlist Operations 🎶")
    print("1. Add Song")
    print("2. Delete Song")
    print("3. Move Song")
    print("4. Reverse Playlist")
    print("5. Display Playlist")
    print("0. Back to Main Menu")

# this function shows the playback history (stack) actions
def show_playback_menu():
    print("\n🎬 Playback History Options")
    print("1. Play a Song")                   # pushes song to stack
    print("2. Undo Last Played Song")        # pops last played from stack
    print("3. Show Playback History")        # prints all songs in stack
    print("0. Back to Main Menu")

# this function handles all playlist operations like add, delete, move, etc.
def handle_playlist_operations(playlist):
    while True:
        show_playlist_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # get song details from user and add it to playlist
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            duration = input("Enter duration (mm:ss): ")
            playlist.add_song(title, artist, duration)

        elif choice == "2":
            # delete song by index
            try:
                index = int(input("Enter index of song to delete: "))
                playlist.delete_song(index - 1)  # user enters 1-based index
            except ValueError:
                print("Please enter a valid index.")

        elif choice == "3":
            # move a song from one index to another
            try:
                from_index = int(input("Enter current index of song: ")) - 1
                to_index = int(input("Enter new index to move it to: ")) - 1
                playlist.move_song(from_index, to_index)
            except ValueError:
                print("Please enter valid indices.")

        elif choice == "4":
            # reverse the playlist
            playlist.reverse_playlist()

        elif choice == "5":
            # display all songs
            playlist.display()

        elif choice == "0":
            # go back to main menu
            break

        else:
            print("Invalid choice. Try again.")

# this function handles the playback history stack (play, undo, view)
def handle_playback_history(playlist, history):
    while True:
        show_playback_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # play a song from playlist (push to stack)
            playlist.display()
            try:
                index = int(input("Enter index of song to play: ")) - 1
                current = playlist.head
                for _ in range(index):
                    if current:
                        current = current.next
                if current:
                    history.play_song(current)  # push to stack
                else:
                    print("❌ Invalid song index.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "2":
            # undo the last played song (pop from stack)
            song = history.undo_last_play()
            if not song:
                print("No song to undo.")

        elif choice == "3":
            # show all recently played songs
            history.show_history()

        elif choice == "0":
            # return to main menu
            break

        else:
            print("Invalid choice. Try again.")

# this is the main function that starts the application
def main():
    playlist = Playlist("Playwise Playlist 1")     # create playlist
    history = PlaybackHistory()                    # create playback stack

    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            handle_playlist_operations(playlist)

        elif choice == "2":
            handle_playback_history(playlist, history)

        elif choice == "3":
            print("Song Rating Tree module coming soon (BST).")

        elif choice == "4":
            print("Instant Lookup module coming soon (HashMap).")

        elif choice == "5":
            print("Sorting module coming soon (Merge/Quick/Heap Sort).")

        elif choice == "6":
            print("Dashboard snapshot module coming soon.")

        elif choice == "7":
            print("Pinned Songs Shuffle logic coming soon.")

        elif choice == "8":
            print("Playlist Summary generator coming soon.")

        elif choice == "0":
            print("👋 Exiting PlayWise. See you next time!")
            break

        else:
            print("Invalid choice. Try again.")

# program starts here
if __name__ == "__main__":
    main()
