from collections import deque
import heapq

class File:
    def __init__(self, name, size, created_at):
        self.name = name
        self._size = size
        self.created_at = created_at
        self._validate_size()

    def _validate_size(self):
        if self._size < 0:
            raise ValueError("Size cannot be negative")

    def get_size(self):
        return self._size

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []  # List: Ordered collection of files

    def add_file(self, file_obj):
        if not isinstance(file_obj, File):
            raise ValueError("Only File objects allowed")
        self.files.append(file_obj)

    def get_file_metadata(self):
        # Dictionary: Store file metadata
        return {f.name: {"size": f.get_size(), "created_at": f.created_at} for f in self.files}

    def get_unique_extensions(self):
        # Set: Track unique file extensions
        return {f.name.rsplit(".", 1)[1] if "." in f.name else "" for f in self.files}

    def get_largest_file(self):
        # Heap: Find file with maximum size
        if not self.files:
            return None
        # Create max heap by using negative sizes
        heap = [(-f.get_size(), f.name) for f in self.files]
        heapq.heapify(heap)
        max_size, max_name = heapq.heappop(heap)
        return max_name, -max_size  # Return name and original size

class User:
    def __init__(self, username):
        self.username = username
        self.directories = {}  # Dictionary: Organize directories
        self.expiry_queue = deque()  # Deque: Track file expirations

    def create_directory(self, dir_name):
        if not dir_name:
            raise ValueError("Directory name cannot be empty")
        self.directories[dir_name] = Directory(dir_name)

    def add_file_to_directory(self, dir_name, file_obj):
        if dir_name not in self.directories:
            raise ValueError(f"Directory {dir_name} not found")
        if not isinstance(file_obj, File):
            raise ValueError("Invalid file object")
        self.directories[dir_name].add_file(file_obj)
        self.expiry_queue.append((file_obj.name, file_obj.created_at))

# Example usage
if __name__ == "__main__":
    # Create a user
    user = User("alice")

    # Create a directory
    user.create_directory("Docs")

    # Add files
    file1 = File("doc1.txt", 1024, "2025-05-28")
    file2 = File("doc2.txt", 2048, "2025-05-28")
    file3 = File("image.png", 512, "2025-05-28")
    user.add_file_to_directory("Docs", file1)
    user.add_file_to_directory("Docs", file2)
    user.add_file_to_directory("Docs", file3)

    # Test data structures
    docs_dir = user.directories["Docs"]
    
    # Dictionary: File metadata
    print("File Metadata:", docs_dir.get_file_metadata())
    # Output: {'doc1.txt': {'size': 1024, 'created_at': '2025-05-28'}, ...}

    # Set: Unique extensions
    print("Unique Extensions:", docs_dir.get_unique_extensions())
    # Output: {'txt', 'png'}

    # Heap: Largest file
    print("Largest File:", docs_dir.get_largest_file())
    # Output: ('doc2.txt', 2048)

    # Deque: Expiry queue
    print("Expiry Queue:", list(user.expiry_queue))
    # Output: [('doc1.txt', '2025-05-28'), ('doc2.txt', '2025-05-28'), ('image.png', '2025-05-28')]