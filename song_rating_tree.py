# song_rating_tree.py

# first, we define a node in our binary search tree
# each node represents a rating (from 1 to 5)
class RatingNode:
    def __init__(self, rating):
        self.rating = rating                # the actual rating value (1 to 5)
        self.songs = []                     # this will hold all songs with this rating
        self.left = None                    # pointer to the left (lower ratings)
        self.right = None                   # pointer to the right (higher ratings)

# this is the main class that manages the BST
# it helps us insert and search songs by rating
class RatingBST:
    def __init__(self):
        self.root = None                    # start with an empty tree (no ratings yet)

    # this function is used to add a new song into the BST
    # we give it a song node and a rating (e.g., 5 stars)
    def insert_song(self, song, rating):
        # we call a helper function that does the actual work
        self.root = self._insert(self.root, song, rating)

    # internal function that does the recursive insertion
    def _insert(self, node, song, rating):
        # if we've reached a spot with no node, it means this rating doesn’t exist yet
        # so we create a new rating node here
        if node is None:
            new_node = RatingNode(rating)   # create a new node for this rating
            new_node.songs.append(song)     # add the song to this new rating bucket
            return new_node

        # if the rating is smaller, we move left in the tree
        if rating < node.rating:
            node.left = self._insert(node.left, song, rating)
        # if the rating is greater, we move right
        elif rating > node.rating:
            node.right = self._insert(node.right, song, rating)
        # if the rating already exists, just add the song to the existing list
        else:
            node.songs.append(song)

        return node  # return the unchanged node up the tree

    # this function lets us find and print all songs with a specific rating
    def search_by_rating(self, rating):
        node = self._search(self.root, rating)

        if node is None:
            print(f"\n😕 No songs found with rating {rating}")
        else:
            print(f"\n⭐ Songs with Rating {rating}:")
            for i, song in enumerate(node.songs, 1):
                print(f"{i}. {song.title} by {song.artist}")

    # this is the recursive search function that looks for the rating node
    def _search(self, node, rating):
        # base case: rating not found
        if node is None:
            return None

        # if this is the rating we're looking for, return the node
        if rating == node.rating:
            return node
        # go left for lower rating
        elif rating < node.rating:
            return self._search(node.left, rating)
        # go right for higher rating
        else:
            return self._search(node.right, rating)

    # (optional) this function prints all songs in the tree in rating order
    # we use an in-order traversal for this
    def inorder(self):
        print("\n🌳 All Rated Songs (from lowest to highest rating):")
        self._inorder(self.root)

    # recursive helper for in-order traversal
    def _inorder(self, node):
        if node:
            self._inorder(node.left)  # visit left side first (lower ratings)

            # print songs under this rating
            print(f"\nRating {node.rating}:")
            for song in node.songs:
                print(f"  - {song.title} by {song.artist}")

            self._inorder(node.right)  # then visit right side (higher ratings)
