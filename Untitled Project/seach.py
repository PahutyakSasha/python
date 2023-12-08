import threading
import os
import queue

def search_files(directory, file_queue):
    try:
        for item in os.listdir(directory):
            full_path = os.path.join(directory, item)
            if os.path.isdir(full_path):
                search_files(full_path, file_queue)
            elif full_path.endswith('.txt'):
                file_queue.put(full_path)
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error accessing directory or file: {directory}. Error: {e}")

def process_files(file_queue):
    while not file_queue.empty():
        file_path = file_queue.get()
        print(f"Found .txt file: {file_path}")

def main(search_directory):
    file_queue = queue.Queue()

    search_thread = threading.Thread(target=search_files, args=(search_directory, file_queue))
    search_thread.start()

    search_thread.join()
    process_files(file_queue)
search_directory = "/home/pahutyaksasha/file"
main(search_directory)