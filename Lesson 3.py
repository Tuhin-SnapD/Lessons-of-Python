from datetime import datetime

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

    def get_name(self):
        return self.name

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []

    def add_file(self, file_obj):
        if not isinstance(file_obj, File):
            raise ValueError("Only File objects allowed")
        self.files.append(file_obj)

    def sort_files_by_size_and_name(self):
        """Sort files by size (ascending), then name (alphabetically) for tiebreakers."""
        if not self.files:
            return []
        return sorted(self.files, key=lambda f: (f.get_size(), f.get_name()))

    def parse_filename(self, filename):
        """Parse filename into name and extension."""
        if not filename:
            raise ValueError("Filename cannot be empty")
        return filename.rsplit(".", 1) if "." in filename else (filename, "")

class User:
    def __init__(self, username):
        self.username = username
        self.directories = {}

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

    def check_expired_files(self, dir_name, ttl_days):
        """Check for files in directory older than ttl_days."""
        if dir_name not in self.directories:
            raise ValueError(f"Directory {dir_name} not found")
        if ttl_days < 0:
            raise ValueError("TTL days cannot be negative")
        expired = []
        now = datetime.now()
        for file in self.directories[dir_name].files:
            try:
                created = datetime.strptime(file.created_at, "%Y-%m-%d")
                if (now - created).days > ttl_days:
                    expired.append(file.name)
            except ValueError:
                print(f"Warning: Invalid date format for {file.name}, skipping")
        return expired

# Example usage
if __name__ == "__main__":
    # Create a user
    user = User("alice")

    # Create a directory
    user.create_directory("Docs")

    # Add files
    file1 = File("doc1.txt", 1024, "2025-05-20")
    file2 = File("doc2.txt", 512, "2025-05-27")
    file3 = File("doc3.txt", 512, "2025-05-27")
    user.add_file_to_directory("Docs", file1)
    user.add_file_to_directory("Docs", file2)
    user.add_file_to_directory("Docs", file3)

    # Test algorithms
    docs_dir = user.directories["Docs"]

    # Sorting with custom keys
    sorted_files = docs_dir.sort_files_by_size_and_name()
    print("Sorted Files (size, name):", [f.name for f in sorted_files])
    # Output: ['doc2.txt', 'doc3.txt', 'doc1.txt']

    # String manipulation
    name, ext = docs_dir.parse_filename("doc1.txt")
    print("Parsed Filename:", name, ext)
    # Output: doc1 txt

    # Time comparison
    expired_files = user.check_expired_files("Docs", 7)
    print("Expired Files (TTL 7 days):", expired_files)
    # Output: ['doc1.txt'] (assuming today is 2025-05-28)