# playlist_summary.py

def generate_summary_report(playlist, filename="summary.txt"):
    """
    Time Complexity: O(n), n = number of songs
    Space Complexity: O(n)
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("PlayWise Playlist Summary Report\n")
            file.write("=" * 40 + "\n")
            file.write(f"Playlist Name: {playlist.name}\n")
            file.write(f"Total Songs: {playlist.size}\n\n")

            file.write("Songs:\n")
            file.write("-" * 40 + "\n")

            current = playlist.head
            index = 1
            total_duration = 0
            pinned_count = 0
            longest_song = None
            shortest_song = None

            while current:
                minutes = current.duration // 60
                seconds = current.duration % 60
                duration_str = f"{minutes}:{seconds:02d}"
                pin_status = "Pinned" if getattr(current, "pinned", False) else "Unpinned"

                file.write(f"{index}. {current.title} by {current.artist} ({duration_str}) - {pin_status}\n")

                # accumulate data
                total_duration += current.duration
                pinned_count += 1 if current.pinned else 0

                # track longest/shortest songs
                if not longest_song or current.duration > longest_song.duration:
                    longest_song = current
                if not shortest_song or current.duration < shortest_song.duration:
                    shortest_song = current

                index += 1
                current = current.next

            file.write("-" * 40 + "\n")

            # Summary stats
            avg_duration = total_duration // playlist.size if playlist.size else 0
            avg_min = avg_duration // 60
            avg_sec = avg_duration % 60
            total_min = total_duration // 60
            total_sec = total_duration % 60

            file.write(f"Total Duration: {total_min}:{total_sec:02d}\n")
            file.write(f"Average Song Length: {avg_min}:{avg_sec:02d}\n")
            file.write(f"Pinned Songs: {pinned_count} / {playlist.size}\n")

            if longest_song:
                lm, ls = longest_song.duration // 60, longest_song.duration % 60
                file.write(f"Longest Song: {longest_song.title} ({lm}:{ls:02d})\n")
            if shortest_song:
                sm, ss = shortest_song.duration // 60, shortest_song.duration % 60
                file.write(f"Shortest Song: {shortest_song.title} ({sm}:{ss:02d})\n")

        print(f"Summary report generated successfully in '{filename}'.")

    except Exception as e:
        print("Failed to generate summary report:", e)


# optional wrapper for input prompt
def handle_summary_export(playlist):
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    filename = input("Enter filename to export summary (default is 'summary.txt'): ").strip()
    if not filename:
        filename = "summary.txt"
    generate_summary_report(playlist, filename)
