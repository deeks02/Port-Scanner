import socket
import threading
import sys
from queue import Queue

try:
    target = input("Enter the target IP or hostname: ")
    if target.lower() == 'q':
        print("Exiting program.")
        sys.exit()
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
except ValueError:
    print("Invalid input. Please enter valid numbers for ports.")
    sys.exit()

queue = Queue()
lock = threading.Lock()

def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((target, port)) == 0:
                try:
                    protocol = socket.getservbyport(port)
                except OSError:
                    protocol = "Unknown"
                with lock:
                    print(f"Port {port} is open ({protocol})")
    except Exception as e:
        pass

def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()

def main():
    for port in range(start_port, end_port + 1):
        queue.put(port)

    thread_list = []
    for _ in range(100):
        t = threading.Thread(target=worker)
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()

if __name__ == "__main__":
    main()