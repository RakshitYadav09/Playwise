# dashboard.py

# this function generates a live dashboard report of the current playlist
def export_snapshot(playlist, filename="dashboard.txt"):
    """
    Time Complexity: O(n log n), n = number of songs (due to sorting for top songs)
    Space Complexity: O(n)
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("PlayWise Playlist Dashboard Snapshot\n")
            file.write("=" * 40 + "\n")
            file.write(f"Playlist Name: {playlist.name}\n")
            file.write(f"Total Songs: {playlist.size}\n\n")

            file.write("Songs:\n")
            file.write("-" * 40 + "\n")

            current = playlist.head
            index = 1
            total_duration = 0
            song_list = []

            while current:
                minutes = current.duration // 60
                seconds = current.duration % 60
                formatted_duration = f"{minutes}:{seconds:02d}"
                file.write(f"{index}. {current.title} by {current.artist} ({formatted_duration})\n")
                total_duration += current.duration
                song_list.append((current.title, current.artist, current.duration))
                current = current.next
                index += 1

            file.write("-" * 40 + "\n")

            # total and average
            avg = total_duration // playlist.size if playlist.size else 0
            avg_min = avg // 60
            avg_sec = avg % 60
            total_min = total_duration // 60
            total_sec = total_duration % 60

            file.write(f"Total Playlist Duration: {total_min}:{total_sec:02d}\n")
            file.write(f"Average Song Length: {avg_min}:{avg_sec:02d}\n")

            # optional: show top 3 longest songs
            file.write("\nTop 3 Longest Songs:\n")
            song_list.sort(key=lambda x: x[2], reverse=True)
            for i, song in enumerate(song_list[:3], start=1):
                m, s = song[2] // 60, song[2] % 60
                file.write(f"{i}. {song[0]} by {song[1]} - {m}:{s:02d}\n")

        print(f"Snapshot exported successfully to '{filename}'.")

    except Exception as e:
        print("Something went wrong while exporting:", e)


# optional wrapper to ask user for file name
def handle_dashboard_export(playlist):
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    filename = input("Enter filename to export (leave blank for 'dashboard.txt'): ").strip()
    if not filename:
        filename = "dashboard.txt"
    export_snapshot(playlist, filename)
