from datetime import datetime

class File:
    def __init__(self, name, size, created_at):
        self._validate_inputs(name, size, created_at)
        self.name = name
        self._size = size  # Private for encapsulation
        self.created_at = created_at

    def _validate_inputs(self, name, size, created_at):
        """Validate inputs to ensure they meet requirements."""
        if not name:
            raise ValueError("File name cannot be empty")
        if not isinstance(size, (int, float)) or size < 0:
            raise ValueError("Size must be a non-negative number")
        if not isinstance(created_at, str):
            raise ValueError("Created_at must be a string")

    def get_size(self):
        """Get the file size."""
        return self._size

    def get_name(self):
        """Get the file name."""
        return self.name

    def upload(self):
        """Simulate uploading the file."""
        return f"Uploading {self.name} ({self._size} bytes)"

    def copy(self, new_name):
        """Create a copy of the file with a new name."""
        if not new_name:
            raise ValueError("New name cannot be empty")
        return File(new_name, self._size, self.created_at)

class Directory:
    def __init__(self, name):
        self._validate_directory_name(name)
        self.name = name
        self.files = []

    def _validate_directory_name(self, name):
        """Validate directory name."""
        if not name:
            raise ValueError("Directory name cannot be empty")

    def add_file(self, file_obj):
        """Add a file to the directory."""
        if not isinstance(file_obj, File):
            raise ValueError("Only File objects allowed")
        self.files.append(file_obj)

    def calculate_total_size(self):
        """Calculate total size of all files in the directory."""
        return sum(file.get_size() for file in self.files)

    def sort_files_by_size_and_name(self):
        """Sort files by size (ascending), then name (alphabetically)."""
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
        self._validate_username(username)
        self.username = username
        self.directories = {}

    def _validate_username(self, username):
        """Validate username."""
        if not username:
            raise ValueError("Username cannot be empty")

    def create_directory(self, dir_name):
        """Create a new directory."""
        self._validate_directory_name(dir_name)
        self.directories[dir_name] = Directory(dir_name)

    def add_file_to_directory(self, dir_name, file_obj):
        """Add a file to a specific directory."""
        self._validate_directory_exists(dir_name)
        if not isinstance(file_obj, File):
            raise ValueError("Invalid file object")
        self.directories[dir_name].add_file(file_obj)

    def _validate_directory_exists(self, dir_name):
        """Check if directory exists."""
        if dir_name not in self.directories:
            raise ValueError(f"Directory {dir_name} not found")

    def check_expired_files(self, dir_name, ttl_days):
        """Check for files in directory older than ttl_days."""
        self._validate_directory_exists(dir_name)
        if not isinstance(ttl_days, (int, float)) or ttl_days < 0:
            raise ValueError("TTL days must be a non-negative number")
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
    user.create_directory("Documents")

    # Add files
    try:
        file1 = File("doc1.txt", 1024, "2025-05-20")
        file2 = File("doc2.txt", 512, "2025-05-27")
        file3 = File("image.png", 512, "2025-05-27")
        user.add_file_to_directory("Documents", file1)
        user.add_file_to_directory("Documents", file2)
        user.add_file_to_directory("Documents", file3)

        # Test clean coding practices
        docs_dir = user.directories["Documents"]

        # Descriptive names and modular methods
        print("Total Size:", docs_dir.calculate_total_size())
        # Output: 2048

        # Sorting with custom keys
        sorted_files = docs_dir.sort_files_by_size_and_name()
        print("Sorted Files:", [f.get_name() for f in sorted_files])
        # Output: ['doc2.txt', 'image.png', 'doc1.txt']

        # String manipulation
        name, ext = docs_dir.parse_filename("doc1.txt")
        print("Parsed Filename:", name, ext)
        # Output: doc1 txt

        # Time comparison with defensive programming
        expired_files = user.check_expired_files("Documents", 7)
        print("Expired Files (TTL 7 days):", expired_files)
        # Output: ['doc1.txt'] (assuming today is 2025-05-28)

    except ValueError as e:
        print(f"Error: {e}")