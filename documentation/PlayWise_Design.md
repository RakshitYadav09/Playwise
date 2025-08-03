---
# PlayWise: Smart Music Playlist Management Engine

## Table of Contents
1. Introduction
2. High-Level Architecture
3. Data Structures & Algorithms
4. Module Breakdown
5. System Flowcharts & Diagrams
6. Pseudocode for Major Algorithms
7. Design Trade-offs & Justifications
8. Benchmarks & Test Results
9. Conclusion

---

## 1. Introduction
PlayWise is designed to be a robust backend engine for personalized music playlist management. It supports real-time playlist manipulation, recommendations, memory-efficient search, and smart sorting. The system leverages classic data structures and algorithms to deliver a feature-rich, optimized experience.

## 2. High-Level Architecture

**Modules:**
- Playlist Engine (Doubly Linked List)
- Playback History (Stack)
- Song Rating Tree (BST)
- Instant Song Lookup (HashMap)
- Sorting (Merge/Quick Sort)
- Pinned Songs (Array + HashMap)
- Playlist Summary & Dashboard (Aggregation)

**Flow:**
User interacts with a menu-driven interface. Each module is isolated but can share data (e.g., playlist syncs with lookup and rating tree). All operations are performed in-memory for speed and simplicity.

## 3. Data Structures & Algorithms

### Playlist Engine
- **Doubly Linked List:** Each song is a node. Allows O(1) add/remove at ends, O(n) for indexed operations.

### Playback History
- **Stack:** Tracks recently played songs. Supports O(1) push/pop for undo.

### Song Rating Tree
- **Binary Search Tree:** Each node is a rating bucket (1-5). Fast insert/search by rating. Songs with same rating stored in a list.

### Instant Song Lookup
- **HashMap (Dictionary):** Maps song titles (case-insensitive) to song nodes. Enables O(1) search, add, delete.

### Sorting
- **Merge Sort / Quick Sort:** Custom implementations for linked lists. Sort by title or duration. Merge Sort is stable; Quick Sort is faster on average but can degrade to O(n^2).

### Pinned Songs
- **Array + HashMap:** Tracks pinned indices. Shuffle only affects unpinned songs.

### Summary & Dashboard
- **Aggregation:** Uses traversal, sorting, and frequency maps to generate reports.

## 4. Module Breakdown

### Playlist Engine
- Add, delete, move, reverse songs.
- Syncs with lookup and rating tree.

### Playback History
- Play a song (push to stack).
- Undo last play (pop from stack, re-queue).

### Song Rating Tree
- Rate songs (insert into BST).
- Search by rating, show all rated songs.
- Delete song by ID/title from BST.

### Instant Song Lookup
- Add, find, delete songs by title (case-insensitive).

### Sorting
- Sort playlist by title/duration using merge or quick sort.

### Pinned Songs
- Pin/unpin songs by index.
- Shuffle only unpinned songs.

### Summary & Dashboard
- Export snapshot: top longest songs, stats, rating counts.
- Generate summary: genre distribution, playtime, artist count.

## 5. System Flowcharts & Diagrams

```
User Menu
   |
   v
Playlist Engine <--> Song Lookup
   |
   v
Playback History
   |
   v
Song Rating Tree
   |
   v
Sorting
   |
   v
Pinned Songs
   |
   v
Summary/Dashboard
```

![Playlist Engine Diagram](https://i.imgur.com/2QwQw2B.png)

## 6. Pseudocode for Major Algorithms

### Add Song to Playlist
```
function add_song(title, artist, duration):
    node = new SongNode(title, artist, duration)
    if playlist.head is None:
        playlist.head = playlist.tail = node
    else:
        playlist.tail.next = node
        node.prev = playlist.tail
        playlist.tail = node
    size += 1
```

### Merge Sort for Playlist
```
function merge_sort(head):
    if head is None or head.next is None:
        return head
    left, right = split(head)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
```

### Pinning Songs
```
function shuffle_with_pins(playlist):
    unpinned = [node for node in playlist if not node.pinned]
    shuffle(unpinned)
    reassign unpinned data to original positions
```

## 7. Design Trade-offs & Justifications

- **Linked List for Playlist:** Chosen for efficient reordering and reversal. Array would be faster for indexed access but slower for insert/delete.
- **Stack for History:** Simple, fast undo. Queue not needed as order is LIFO.
- **BST for Ratings:** Allows fast search and range queries. HashMap would lose ordering.
- **HashMap for Lookup:** O(1) access, case-insensitive for user convenience.
- **Custom Sorting:** Built-in sort is not suitable for linked lists; custom merge/quick sort is optimal.
- **Pinned Songs:** Array + HashMap allows flexible pinning and shuffling.

## 8. Benchmarks & Test Results

| Operation         | Time Complexity | Space Complexity | Notes                       |
|-------------------|----------------|------------------|-----------------------------|
| Add Song          | O(1)           | O(1)             | Doubly linked list          |
| Delete Song       | O(n)           | O(1)             | Indexed delete              |
| Move Song         | O(n)           | O(1)             | Indexed move                |
| Reverse Playlist  | O(n)           | O(1)             | Pointer swap                |
| Play Song         | O(1)           | O(1)             | Stack push                  |
| Undo Last Play    | O(1)           | O(1)             | Stack pop                   |
| Rate Song         | O(h)           | O(h)             | BST insert                  |
| Search by Rating  | O(h+k)         | O(1)             | h=height, k=songs in bucket |
| Lookup Song       | O(1)           | O(1)             | HashMap                     |
| Sort Playlist     | O(n log n)     | O(log n)         | Merge/Quick sort            |
| Pin/Unpin Song    | O(n)           | O(1)             | Indexed access              |
| Shuffle           | O(n)           | O(n)             | Only unpinned shuffled      |

**Test Cases:**
- All modules tested with edge cases (empty playlist, duplicate songs, invalid input).
- Lookup is case-insensitive and robust.
- Sorting verified for both title and duration.
- Pinning and shuffling tested for correct constraints.

## 9. Conclusion

PlayWise demonstrates how classic data structures and algorithms can be combined to build a modern, efficient music playlist engine. The modular design ensures maintainability and extensibility, while careful trade-offs deliver both performance and user-friendly features.

---
