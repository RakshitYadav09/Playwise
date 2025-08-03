# Import all required modules and their menu handlers
from playlist_engine import Playlist, handle_playlist_operations
from playback_history import PlaybackHistory, handle_playback_history
from song_rating_tree import RatingBST, handle_song_ratings
from song_lookup import SongLookup, handle_song_lookup
from sort_utils import handle_sort_menu
from dashboard import handle_dashboard_export
from pinned_songs import handle_shuffle_menu
from playlist_summary import handle_summary_export




# This function shows the main menu options for the user
def show_main_menu():
    print("\nWelcome to the PlayWise Smart Music Engine")
    print("============== MAIN MENU ==============")
    print("1. Playlist Operations")
    print("2. Playback History (Undo Last Played Song)")
    print("3. Song Rating (BST-based Recommendations)")
    print("4. Instant Song Lookup (Hash Map)")
    print("5. Sort Playlist (Merge/Quick Sort)")
    print("6. Export Live Dashboard Snapshot")
    print("7. Shuffle with Pinned Songs")
    print("8. Generate Playlist Summary Report")
    print("0. Exit")
    print("=======================================")

# Main function that runs the music engine
def main():
    # Initialize core modules
    playlist = Playlist("Playwise Playlist 1")
    history = PlaybackHistory()
    rating_tree = RatingBST()
    lookup = SongLookup()

    # --- Demo Songs: Pre-populate playlist with real and creative choices ---
    demo_songs = [
        ("Blinding Lights", "The Weeknd", "3:20"),
        ("Shape of You", "Ed Sheeran", "3:53"),
        ("Levitating", "Dua Lipa", "3:23"),
        ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "4:30"),
        ("Bohemian Rhapsody", "Queen", "5:55"),
        ("Bad Guy", "Billie Eilish", "3:14"),
        ("Believer", "Imagine Dragons", "3:24"),
        ("Rolling in the Deep", "Adele", "3:48"),
        ("Can't Stop the Feeling!", "Justin Timberlake", "3:56"),
        ("Closer", "The Chainsmokers ft. Halsey", "4:05"),
        # A few creative ones for fun:
    ]
    for title, artist, duration in demo_songs:
        playlist.add_song(title, artist, duration)
        lookup.add_song(playlist.tail)

    # Start the application loop
    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        # Module 1: Playlist Operations (add, delete, move, etc.)
        if choice == "1":
            handle_playlist_operations(playlist, lookup)

        # Module 2: Playback History (stack-based undo feature)
        elif choice == "2":
            handle_playback_history(playlist, history)

        # Module 3: Song Ratings using Binary Search Tree
        elif choice == "3":
            handle_song_ratings(playlist, rating_tree)

        # Module 4: Instant Song Lookup using Hash Map
        elif choice == "4":
            handle_song_lookup(lookup)
            
        elif choice == "5":
            handle_sort_menu(playlist)
            
        elif choice == "6":
            handle_dashboard_export(playlist)

        elif choice == "7":
            handle_shuffle_menu(playlist)

        elif choice == "8":
            handle_summary_export(playlist)


        # Exit the program
        elif choice == "0":
            print("Exiting PlayWise. Thank you for using the app.")
            break

        # Handle invalid menu choices
        else:
            print("Invalid choice. Please try again.")

# This ensures the program only runs when executed directly
if __name__ == "__main__":
    main()
