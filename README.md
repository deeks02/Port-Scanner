# Port Scanner

## About This Project:
This project is a multithreaded port scanner written in Python. It allows you to scan a range of ports on a target host (IP address or hostname) to identify which ports are open and their associated services. The scanner uses multithreading to speed up the process and can handle large port ranges efficiently.

## Features:
* __Multithreaded Scanning__: Utilizes 100 threads by default to perform fast and efficient scanning.
* __Service Detection__: Attempts to resolve the service running on an open port using the socket.getservbyport method.
* __Custom Port Range__: Allows you to specify the starting and ending ports for the scan.
* __Graceful Input Handling__: Ensures proper handling of invalid inputs like non-numeric ports or unreachable hosts.

## How It Works:
1. __Input__: The program prompts the user for:
   * Target IP address or hostname.
   * Starting and ending port numbers.
2. __Queue-Based Scanning__: Each port in the specified range is added to a queue. Worker threads pick ports from the queue and attempt to connect to them.
3. __Output__: The program displays a list of open ports along with their detected services (if available).

> [!CAUTION]
> ***Legal Disclaimer***: This python script is intended for educational purposes only. Do not attempt to use this script with malicious intent. 
