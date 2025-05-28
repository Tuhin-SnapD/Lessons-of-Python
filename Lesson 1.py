# final.py for Lesson 1: Object-Oriented Programming

class File:
    def __init__(self, name, size, created_at):
        self.name = name
        self._size = size  # Private by convention
        self.created_at = created_at
        self._validate_size()

    def _validate_size(self):
        if self._size < 0:
            raise ValueError("Size cannot be negative")

    def get_size(self):
        return self._size

    def upload(self):
        if not self.name:
            raise ValueError("File name cannot be empty")
        return f"Uploading {self.name} ({self._size} bytes)"

    def copy(self, new_name):
        if not new_name:
            raise ValueError("New name cannot be empty")
        return File(new_name, self._size, self.created_at)


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []  # Composition: Directory contains Files

    def add_file(self, file_obj):
        if not isinstance(file_obj, File):
            raise ValueError("Only File objects allowed")
        self.files.append(file_obj)

    def total_size(self):
        return sum(file.get_size() for file in self.files)


class User:
    def __init__(self, username):
        self.username = username
        self.directories = {}  # Organize directories by name

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


# Example usage
if __name__ == "__main__":
    # Create a user
    user = User("alice")

    # Create a directory
    user.create_directory("Docs")

    # Create and add files
    file1 = File("doc1.txt", 1024, "2025-05-28")
    file2 = File("doc2.txt", 2048, "2025-05-28")
    user.add_file_to_directory("Docs", file1)
    user.add_file_to_directory("Docs", file2)

    # Test functionality
    print(file1.upload())  # Output: Uploading doc1.txt (1024 bytes)
    copied_file = file1.copy("doc1_copy.txt")
    print(copied_file.name)  # Output: doc1_copy.txt
    print(user.directories["Docs"].total_size())  # Output: 3072