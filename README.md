# Port Scanner

## About This Project:
This project is a multithreaded port scanner written in Python. It allows you to scan a range of ports on a target host (IP address or hostname) to identify which ports are open and their associated services. The scanner uses multithreading to speed up the process and can handle large port ranges efficiently.

## Features:
* Multithreaded Scanning: Utilizes 100 threads by default to perform fast and efficient scanning.
* Service Detection: Attempts to resolve the service running on an open port using the socket.getservbyport method.
*  Custom Port Range: Allows you to specify the starting and ending ports for the scan.
*  Graceful Input Handling: Ensures proper handling of invalid inputs like non-numeric ports or unreachable hosts.

## How It Works:
1. Input: The program prompts the user for:
   * Target IP address or hostname.
   * Starting and ending port numbers.
2. Queue-Based Scanning: Each port in the specified range is added to a queue. Worker threads pick ports from the queue and attempt to connect to them.
3. Output: The program displays a list of open ports along with their detected services (if available).

> Legal Disclaimer: This python script is intended for educational purposes only. Do not attempt to use this script with malicious intent. 
