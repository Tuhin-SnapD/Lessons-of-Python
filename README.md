# Lessons-of-Python

## File Management System Learning Repository

This repository contains four Python files (Lessons 1–4.py) designed to teach key programming concepts through a simple file management system. Each file focuses on a specific lesson, building on the previous ones to create a cohesive learning experience. The system models `File`, `Directory`, and `User` classes to simulate file operations like uploading, sorting, and expiration checking.

## Repository Structure

- `Lesson 1.py`: Focuses on **Object-Oriented Programming (OOP)** concepts, including class/object design, encapsulation, composition over inheritance, and data organization.
- `Lesson 2.py`: Demonstrates **built-in data structures** (dictionary, list, set, heap, deque) for managing file metadata, unique extensions, largest files, and expiration queues.
- `Lesson 3.py`: Implements **basic algorithms** for sorting files by size and name, parsing filenames, and checking file expiration using time comparison.
- `Lesson 4.py`: Emphasizes **clean coding habits**, including descriptive names, modular methods, edge case handling, defensive programming, and avoiding premature optimization.

## Prerequisites

- Python 3.6 or higher
- No external libraries are required, as all code uses built-in Python modules (`datetime`, `collections`, `heapq`).

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Run any `final.py` file:
   ```bash
   python Lesson 1.py
   python Lesson 2.py
   python Lesson 3.py
   python Lesson 4.py
   ```

3. Each file includes example usage in the `if __name__ == "__main__":` block, which demonstrates the functionality with sample outputs.

## Lesson Details

### Lesson 1: Object-Oriented Programming
- **Concepts**: Class/object design, encapsulation, composition over inheritance, data organization.
- **Features**: `File` class with `upload` and `copy` methods, `Directory` class with file list, `User` class to manage directories.
- **Example Output**:
  ```
  Uploading doc1.txt (1024 bytes)
  doc1_copy.txt
  3072
  ```

### Lesson 2: Built-in Data Structures
- **Concepts**: Dictionary (file metadata), list (file order), set (unique extensions), heap (largest file), deque (expiration queue).
- **Features**: Methods to retrieve metadata, unique extensions, and the largest file using a max heap.
- **Example Output**:
  ```
  File Metadata: {'doc1.txt': {'size': 1024, 'created_at': '2025-05-28'}, ...}
  Unique Extensions: {'txt', 'png'}
  Largest File: ('doc2.txt', 2048)
  ```

### Lesson 3: Basic Algorithms
- **Concepts**: Sorting with custom keys (size, then name), string manipulation (filename parsing), time comparison (TTL checks).
- **Features**: Sort files, parse filenames into name/extension, check expired files based on TTL.
- **Example Output**:
  ```
  Sorted Files (size, name): ['doc2.txt', 'doc3.txt', 'doc1.txt']
  Parsed Filename: doc1 txt
  Expired Files (TTL 7 days): ['doc1.txt']
  ```

### Lesson 4: Clean Coding Habits
- **Concepts**: Descriptive names, modular methods, edge case handling, defensive programming, avoiding premature optimization.
- **Features**: Refactored code with clear names (e.g., `calculate_total_size`), modular validation functions, and robust error handling.
- **Example Output**:
  ```
  Total Size: 2048
  Sorted Files: ['doc2.txt', 'image.png', 'doc1.txt']
  Parsed Filename: doc1 txt
  Expired Files (TTL 7 days): ['doc1.txt']
  ```

## Notes
- The code assumes the current date is May 28, 2025, for time-based calculations (e.g., expiration checks).
- Each `.py` file is self-contained and can be run independently.
- The files build on each other, with Lesson 4 being the most polished in terms of clean coding practices.

## Contributing
Feel free to fork the repository, make improvements, or suggest new features via pull requests. Ensure any changes follow the clean coding principles demonstrated in Lesson 4.

## License
This project is licensed under the MIT License.