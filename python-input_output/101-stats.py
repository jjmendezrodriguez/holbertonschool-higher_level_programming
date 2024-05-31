#!/usr/bin/python3
"""
This script reads log entries from stdin and computes metrics based on the contents.
It tracks total file size and the number of occurrences of each HTTP status code.
Every 10 lines and upon receiving a Ctrl+C signal, it prints these metrics.
"""

import sys
import signal

def signal_handler(sig, frame):
    """Handles the Ctrl+C signal to print the statistics before exiting."""
    print_stats()
    sys.exit(0)

def print_stats():
    """Prints the accumulated statistics for file size and status codes."""
    print("Total file size: File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Dictionary to track status codes
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0  # Total size of files processed
line_count = 0  # Number of lines processed

try:
    # Process each line from stdin
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 2:
            continue

        # Extract status code and file size assuming a specific log format
        status = int(parts[-2])
        size = int(parts[-1])

        # Update total file size and status code count
        total_size += size
        if status in status_codes:
            status_codes[status] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Optionally, handle a KeyboardInterrupt if not caught by the signal
    print_stats()
finally:
    # Optional: Do any cleanup here if necessary
    pass
