class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        
class playlist:
    def __init__(self):
        self.head = None
    
    def add_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        print(f"lagu '{title} ditambahkan ke playlist")